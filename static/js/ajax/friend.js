/**
 * Created by FRAMGIA\nguyen.huy.quyet on 06/01/2016.
 */

function friend_add(user_id) {
    $.ajax({
        url: 'friend/friend/add',
        type: 'POST',
        data: {
            user_id: user_id
        },
        success: function (json) {
            if (json.result) {
                $('#friend_status').html(json.html);
            } else {
                alert('Error submit data');
            }
        },
        error: function () {
            alert('Error submit data');
        }
    });
}


function friend_cancel_request(user_id) {
    $.ajax({
        url: 'friend/friend/cancel_request',
        type: 'POST',
        data: {
            user_id: user_id
        },
        success: function (json) {
            if (json.result) {
                $('#friend_status').html(json.html);
            } else {
                alert('Error submit data');
            }
        },
        error: function () {
            alert('Error submit data');
        }
    });
}

function friend_not_now(user_id) {
    $.ajax({
        url: 'friend/friend/friend_not_now',
        type: 'POST',
        data: {
            user_id: user_id
        },
        success: function (json) {
            if (json.result) {
                $('#friend_status').html(json.html);
            } else {
                alert('Error submit data');
            }
        },
        error: function () {
            alert('Error submit data');
        }
    });
}


function friend_accept(user_id) {
    $.ajax({
        url: 'friend/friend/friend_accept',
        type: 'POST',
        data: {
            user_id: user_id
        },
        success: function (json) {
            if (json.result) {
                $('#friend_status').html(json.html);
            } else {
                alert('Error submit data');
            }
        },
        error: function () {
            alert('Error submit data');
        }
    });
}

function friend_remove(user_id) {
    $.ajax({
        url: 'friend/friend/friend_remove',
        type: 'POST',
        data: {
            user_id: user_id
        },
        success: function (json) {
            if (json.result) {
                $('#friend_status').html(json.html);
            } else {
                alert('Error submit data');
            }
        },
        error: function () {
            alert('Error submit data');
        }
    });
}