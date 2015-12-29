/**
 * Created by FRAMGIA\nguyen.huy.quyet on 28/12/2015.
 */

function create_post_status(user_id) {
    var content_post = Trim($('#write_status_home_' + user_id).val());
    if (content_post == '') {
        return false
    } else {
        $.ajax({
            url: '/post/create_post_home',
            type: 'POST',
            data: {
                //review_id: review_id,
                content_post: content_post
            },
            success: function (json) {
                $('#write_status_home_' + user_id).val('');
                $('#view_post_' + id).append(json.html);
            },
            error: function (json) {
            }
        })
    }

}

function like_post(post_id) {
    $.ajax({
        url: '',
        type: 'POST',
        data: {
            post_id: post_id
        },
        success: function (json) {

        },
        error: function (json) {

        }
    })
}