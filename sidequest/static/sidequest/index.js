const menuContainer = document.getElementById('menu-container');
const menuTrigger = document.getElementById('menu-trigger');

menuTrigger.addEventListener('click', () => {
    if (menuContainer.style.left === '0px') {
        menuContainer.style.left = '-250px';
        menuTrigger.style.color = "black"
    } else {
        menuContainer.style.left = '0px';
        menuTrigger.style.color = "white"
    }
});