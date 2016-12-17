onload = function () {
    var message_div = document.getElementsByClassName('messages');
    if(message_div){
        for(var i = 0; i <= message_div.length; i++){
            message_div[i].addEventListener('click', function(){
                this.remove()
            })
        }
    }
};
