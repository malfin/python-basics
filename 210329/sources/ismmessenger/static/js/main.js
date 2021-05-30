let REFRESH_TIMEOUT = 2500;
let $dialogMessagesDOM;

function messageRender(message) {
    let domMessage = $('.message-' + message.pk);
    let messageText;
    if (!domMessage.length) {
        let newMessage = document.createElement('ul');
        newMessage.classList.add('message-' + message.pk);
        messageText = message.username + " (" + message.created + ") - " + message.text;
        newMessage.innerHTML = messageText;
        let parent = $dialogMessagesDOM.find('.messages-list');
        parent.prepend(newMessage);
    }
}


window.onload = function () {
    console.log('ready');
    $dialogMessagesDOM = $('.dialog-messages');
    $dialogMessagesDOM.on('click', 'dialog-update', function (e) {
        e.preventDefault();
        $.ajax({
            url: e.target.href,
            success: function (response) {
                let new_messages = response.new_messages;
                if (new_messages) {
                    new_messages.forEach(function (el, idx) {
                        messageRender(el);
                    })
                }
            }
        })
    });
    setInterval(function () {
        $('.dialog-update').trigger("click");
    }, REFRESH_TIMEOUT);
}