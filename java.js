const tg = window.Telegram.WebApp;
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

tg.ready();
tg.expand();

console.log(tg.initDataUnsafe.user);

function clickButton(){
    alert(tg.initDataUnsafe.user);
}

fishing01 = new Image();
fishing01.src = "assets/images/png/Fishing01.png";
fishing01.onload = () => {
    console.log("Картинка загружена!");
    ctx.drawImage(fishing01, 0, 0, 64, 64);
};