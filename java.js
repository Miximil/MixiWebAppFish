const tg = window.Telegram.WebApp;

tg.ready();
tg.expand();

console.log(tg.initDataUnsafe.user);

function clickButton(){
    alert(tg.initDataUnsafe.user);
}