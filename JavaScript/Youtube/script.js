let divs = document.getElementsByClassName('sidebarIkonka');

for (let i = 0; i < divs.length; i++) {
    divs[i].addEventListener('mouseover', function() {
        this.style.backgroundColor = 'rgb(240,240,240)';
    });
    
    divs[i].addEventListener('mouseout', function() {
        this.style.backgroundColor = 'white';
    });
}
