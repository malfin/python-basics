let $dialogMessagesDOM;

function messageRender(message) {
    let domMessage = $('.message-' + message.pk);
    let messageText;
    if (!domMessage.length) {
        let newMessage = document.createElement('li');
        newMessage.classList.add('message-' + message.pk);
        // {{ item.sender.member.username }} {{ item.created }} | {{ item.text|linebreaksbr }}
        messageText = message.username + " (" + message.created + ") | " + message.text;
        newMessage.innerHTML = messageText;
        let parent = $dialogMessagesDOM.find('ul');
        parent.prepend(newMessage);
    }
}


window.onload = function () {
    console.log('ready');
    $('.dialog-messages').on('click', 'a.dialog-update', function (e) {
        e.preventDefault();
        $.ajax({
            url: e.target.href,
            success: function (response) {
                let new_messages = response.new_messages
                if (new_messages) {
                    new_messages.forEach(function (el, idx) {
                        messageRender(el);
                    })
                }
            }
        })
    })
    // нажимает на кнопку "обновить" каждые 5 секунд
    setInterval(function () {
        $('.dialog-update').trigger("click");
    }, 5000);
}