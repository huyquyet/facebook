/**
 * Created by FRAMGIA\nguyen.huy.quyet on 28/12/2015.
 */

function create_post_status(user_post_id) {
    var id_new_post = $('#id_new_post').val();
    var user_home_id = $('#user_id').val();
    var content_post = Trim($('#write_status_home_' + user_home_id).val());

    if (content_post == '') {
        return false
    } else {
        $.ajax({
            url: '/post/create_post_home',
            type: 'POST',
            data: {
                user_home_id: user_home_id,
                content_post: content_post
            },
            success: function (json) {
                $('#write_status_home_' + user_home_id).val('');
                $('#view_post_' + id_new_post).before(json.html);
                $('#id_new_post').val(json.id_new_post);
            },
            error: function (json) {
            }
        })
    }

}

function like_post(post_id) {
    $.ajax({
        url: 'like/post/like',
        type: 'POST',
        data: {
            post_id: post_id
        },
        success: function (json) {
            $('#post-like-' + post_id).html('<button type="button" class="btn btn-link btn-xs text"' +
                'onclick="unlike_post(' + post_id + ')"> Unlike</button>');
            $('#number-like-post-' + post_id).html('<a href="#"> ' + json.total_like_post + ' </a> like this');
        },
        error: function (json) {
            alert('Error submit data')
        }
    });
}

function unlike_post(post_id) {
    $.ajax({
        url: 'like/post/unlike',
        type: 'POST',
        data: {
            post_id: post_id
        },
        success: function (json) {
            $('#post-like-' + post_id).html('<button type="button" class="btn btn-link btn-xs text"' +
                'onclick="like_post(' + post_id + ')"> Like</button>');
            $('#number-like-post-' + post_id).html('<a href="#"> ' + json.total_like_post + ' </a> like this');
        },
        error: function (json) {
            alert('Error submit data')
        }
    });
}

function create_post_comment(post_id) {
    var values = $('#create-comment-post-' + post_id + '-content');
    var content_comment = Trim(values.val());
    if (content_comment == '') {
        return false
    } else {
        $.ajax({
            url: 'comment/create/post',
            type: 'POST',
            data: {
                post_id: post_id,
                content_comment: content_comment
            },
            success: function (json) {
                values.val('');
                $('#view-comments-post-' + post_id).append(json.html);
            },
            error: function (json) {
                alert('Error submit data')
            }
        });
    }
}