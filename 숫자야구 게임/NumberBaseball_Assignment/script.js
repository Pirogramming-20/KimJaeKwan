const resultGame = [];
const selectIndex = createRandomNum();
let remainTry = 9;

const input1 = document.getElementById("number1");
const input2 = document.getElementById("number2");
const input3 = document.getElementById("number3");

//첫번째 input에 자동으로 focus
input1.focus();
function resetInput() {
  input1.value = "";
  input2.value = "";
  input3.value = "";
}

function check_numbers() {
  remainTry--;
  const input1Value = Number(input1.value);
  const input2Value = Number(input2.value);
  const input3Value = Number(input3.value);

  //비어있는 input 있으면 input 전부 비우기
  if (input1.value === "" || input2.value === "" || input3.value === "") {
    resetInput();
    remainTry++;
    return;
  }

  //랜덤 숫자와 입력값 비교
  const result = CompareNum(selectIndex, [
    input1Value,
    input2Value,
    input3Value,
  ]);

  //결과를 리스트로 저장
  resultGame.push({
    input: [input1Value, input2Value, input3Value],
    result,
  });

  //결과 누적해서 출력
  showResult();

  const gameResultImg = document.getElementById("game-result-img");
  const submitBtn = document.querySelector(".submit-button");
  //3S면 성공이미지 출력
  if (result.strike === 3) {
    gameResultImg.src = "./success.png";
    submitBtn.disabled = true;
  }

  //9번 시도 후 정답 못 맞추면 실패이미지 출력
  if (remainTry <= 0) {
    gameResultImg.src = "./fail.png";
    submitBtn.disabled = true;
  }

  input1.focus();
  resetInput();
}

function createRandomNum() {
  let randomIndexArray = [];
  for (let i = 0; i < 3; i++) {
    let randomNum = Math.floor(Math.random() * 10);
    if (randomIndexArray.indexOf(randomNum) === -1) {
      randomIndexArray.push(randomNum);
    } else {
      i--;
    }
  }
  return randomIndexArray;
}

function CompareNum(selectIndex, answerIndex) {
  let strike = 0;
  let ball = 0;
  for (let i = 0; i < 3; i++) {
    if (selectIndex[i] === answerIndex[i]) {
      strike++;
    } else if (answerIndex.includes(selectIndex[i])) {
      ball++;
    }
  }
  return { strike, ball };
}

//결과를 출력! div생성
/* <div class="check-result">
    <div class="left">3 5 6</div>
    :
    <div class="right">
    1
    <div class="strike num-result">S</div>
    1
    <div class="ball num-result">B</div>
    </div>
</div> */
function showResult() {
  const resultDisplay = document.querySelector(".result-display");
  resultDisplay.scrollTop = resultDisplay.scrollHeight;
  resultDisplay.innerHTML = "";

  for (const resultG of resultGame) {
    const checkResult = document.createElement("div");
    checkResult.className = "check-result";

    const left = document.createElement("div");
    left.className = "left";
    left.textContent = resultG.input.join(" ");

    const right = document.createElement("div");
    right.className = "right";

    if (resultG.result.strike === 0 && resultG.result.ball === 0) {
      const outResult = document.createElement("div");
      outResult.className = "out num-result";
      outResult.innerText = "O";
      right.appendChild(outResult);
    } else {
      const strikeNumResult = document.createElement("div");
      strikeNumResult.className = "strike num-result";
      strikeNumResult.innerText = "S";

      const ballNumResult = document.createElement("div");
      ballNumResult.className = "ball num-result";
      ballNumResult.innerText = "B";

      right.textContent = resultG.result.strike;
      right.appendChild(strikeNumResult);
      right.textContent += resultG.result.ball;
      right.appendChild(ballNumResult);
    }
    checkResult.appendChild(left);
    checkResult.textContent += ":";
    checkResult.appendChild(right);

    resultDisplay.appendChild(checkResult);
  }
}
