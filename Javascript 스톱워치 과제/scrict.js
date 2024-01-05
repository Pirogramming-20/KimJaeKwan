let time = document.getElementById("time");
let currentTime = 0;
let second, millisecond;

function printTime() {
  currentTime++;
  time.innerText = transformationTime();
}

function start() {
  printTime();
  timer = setTimeout(start, 1);
}

function stop() {
  if (timer != null) {
    clearTimeout(timer);
  }
  addRecord();
}

function reset() {
  currentTime = 0;
  time.innerText = "00:00";
  stop();
}

function transformationTime() {
  second = parseInt(currentTime / 100);
  millisecond = parseInt(currentTime % 100);

  return (
    String(second).padStart(2, "0") + ":" + String(millisecond).padStart(2, "0")
  );
}

function addRecord() {
    
}
