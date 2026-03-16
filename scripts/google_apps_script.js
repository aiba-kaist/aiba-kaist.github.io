/**
 * AIBA Lab Website - Google Sheets 자동 동기화 스크립트
 * 
 * 이 스크립트를 Google Sheets의 Apps Script에 추가하면
 * 시트 수정 시 자동으로 GitHub Actions가 트리거됩니다.
 * 
 * 설정 방법:
 * 1. Google Sheets에서 확장 프로그램 → Apps Script 클릭
 * 2. 이 코드를 복사하여 붙여넣기
 * 3. GITHUB_TOKEN과 REPO 값을 수정
 * 4. 트리거 설정 (시계 아이콘 → 트리거 추가)
 */

// ============================================
// 설정값 (수정 필요)
// ============================================
const CONFIG = {
  // GitHub Personal Access Token (repo 권한 필요)
  // GitHub → Settings → Developer settings → Personal access tokens → Generate new token
  GITHUB_TOKEN: 'YOUR_GITHUB_TOKEN_HERE',
  
  // GitHub 저장소 정보
  REPO_OWNER: 'aiba-kaist',
  REPO_NAME: 'aiba-kaist.github.io',
  
  // 디바운스 시간 (초) - 연속 수정 시 한 번만 트리거
  DEBOUNCE_SECONDS: 60
};

// ============================================
// GitHub Actions 트리거 함수
// ============================================
function triggerGitHubActions() {
  const url = `https://api.github.com/repos/${CONFIG.REPO_OWNER}/${CONFIG.REPO_NAME}/dispatches`;
  
  const options = {
    method: 'POST',
    headers: {
      'Authorization': `token ${CONFIG.GITHUB_TOKEN}`,
      'Accept': 'application/vnd.github.v3+json',
      'Content-Type': 'application/json'
    },
    payload: JSON.stringify({
      event_type: 'sheets-update'
    }),
    muteHttpExceptions: true
  };
  
  try {
    const response = UrlFetchApp.fetch(url, options);
    const code = response.getResponseCode();
    
    if (code === 204) {
      Logger.log('✅ GitHub Actions triggered successfully');
      SpreadsheetApp.getActive().toast('웹사이트 업데이트가 시작되었습니다! (1-2분 소요)', '🚀 동기화 시작', 5);
    } else {
      Logger.log('❌ GitHub Actions trigger failed: ' + response.getContentText());
      SpreadsheetApp.getActive().toast('동기화 실패: ' + response.getContentText(), '⚠️ 오류', 10);
    }
  } catch (error) {
    Logger.log('❌ Error: ' + error.toString());
    SpreadsheetApp.getActive().toast('동기화 오류: ' + error.toString(), '⚠️ 오류', 10);
  }
}

// ============================================
// 디바운스 처리된 트리거
// ============================================
function onEditDebounced(e) {
  const cache = CacheService.getScriptCache();
  const lastTrigger = cache.get('lastTrigger');
  const now = new Date().getTime();
  
  // 디바운스 체크
  if (lastTrigger && (now - parseInt(lastTrigger)) < CONFIG.DEBOUNCE_SECONDS * 1000) {
    Logger.log('⏳ Debounce: Skipping trigger (too soon after last trigger)');
    return;
  }
  
  // 트리거 시간 저장
  cache.put('lastTrigger', now.toString(), CONFIG.DEBOUNCE_SECONDS + 10);
  
  // 잠시 후 트리거 (추가 수정 대기)
  Utilities.sleep(5000); // 5초 대기
  
  triggerGitHubActions();
}

// ============================================
// 메뉴 추가
// ============================================
function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('🔄 웹사이트 동기화')
    .addItem('지금 동기화', 'triggerGitHubActions')
    .addItem('설정 확인', 'showConfig')
    .addToUi();
}

function showConfig() {
  const message = `
현재 설정:
- Repository: ${CONFIG.REPO_OWNER}/${CONFIG.REPO_NAME}
- 디바운스: ${CONFIG.DEBOUNCE_SECONDS}초
- Token: ${CONFIG.GITHUB_TOKEN.substring(0, 10)}...

GitHub Actions URL:
https://github.com/${CONFIG.REPO_OWNER}/${CONFIG.REPO_NAME}/actions
  `;
  
  SpreadsheetApp.getUi().alert('⚙️ 동기화 설정', message, SpreadsheetApp.getUi().ButtonSet.OK);
}

// ============================================
// 트리거 설정 함수 (한 번만 실행)
// ============================================
function setupTrigger() {
  // 기존 트리거 삭제
  const triggers = ScriptApp.getProjectTriggers();
  triggers.forEach(trigger => {
    if (trigger.getHandlerFunction() === 'onEditDebounced') {
      ScriptApp.deleteTrigger(trigger);
    }
  });
  
  // 새 트리거 생성
  ScriptApp.newTrigger('onEditDebounced')
    .forSpreadsheet(SpreadsheetApp.getActive())
    .onEdit()
    .create();
  
  Logger.log('✅ Trigger setup complete');
  SpreadsheetApp.getActive().toast('자동 동기화가 설정되었습니다!', '✅ 설정 완료', 5);
}
