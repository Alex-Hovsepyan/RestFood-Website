function menuFunc(){
    const nav = document.querySelector('nav')

    if(nav.classList == 'active_nav'){
        nav.classList.remove('active_nav')
    }
    
    else {
        nav.classList.add('active_nav')
    }
}

const header = document.querySelector('header')

window.onscroll = () => {
    if(window.scrollY > 80){
        header.style.backgroundColor = '#000000';
    }
    else {
        header.style.backgroundColor = 'transparent';
    }
}

let swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 30,
    freeMode: true,
    loop : true,
    navigation: {
        nextEl: ".button-next",
        prevEl: ".button-prev",
    },
    autoplay : true,
    breakpoints : {
        992 : {
            slidesPerView : 4,
        },
        600 : {
            slidesPerView : 2
        }
    }
  });

function menuSort(e){
    const active = document.querySelector('.menu_container ul .active')
    const products = document.querySelectorAll('.product')
    if(active != e.target){
        active.classList.remove('active');
        e.target.classList.add('active');
    }

    for(i of products){
        if(e.target.dataset.menu === '*'){
            i.style.display = 'block'
        }
        else if(i.dataset.menu === e.target.dataset.menu){
            i.style.display = 'block'
        }
        else {
            i.style.display = 'none'
        }
    }
}