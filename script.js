for (let i = 0; i < 5; i++) {
  console.log(i);
}

const $menuList = document.getElementById("menu-list");
const $menuInput = document.getElementById("menu-input");
const $addMenuBtn = document.getElementById("add-menu-btn");

function addMenu(event) {
  const li = document.createElement("li");
  li.textContent = $menuInput.value;

  $menuList.append(li);
  $menuInput.value = "";

  console.log(event);
}

$addMenuBtn.addEventListener("click", addMenu);
