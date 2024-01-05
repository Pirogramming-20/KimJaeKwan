let time = document.getElementById("time");
let currentTime = 0;
let second, millisecond;
const recordUl = document.querySelector(".record-ul");

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
  // <li>
  //   <i class="fa-regular fa-circle"></i>
  //   <p>01:74</p>
  //   <i></i>
  // </li>
  const li = document.createElement("li");
  const icon = document.createElement("i");
  icon.className = "fa-regular fa-circle";
  const pauseTime = document.createElement("p");
  pauseTime.innerText = transformationTime();
  const empty = document.createElement("i");

  li.appendChild(icon);
  li.appendChild(pauseTime);
  li.appendChild(empty);
  recordUl.appendChild(li);
}
