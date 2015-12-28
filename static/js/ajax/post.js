/**
 * Created by FRAMGIA\nguyen.huy.quyet on 28/12/2015.
 */

function create_post_status(user_id) {
    var content_post = Trim($('#textarea-write-status_' + user_id).val())
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
                $('#textarea-write-status_' + id).val('');
                $('#view_post_' + id).append(json.html);
            },
            error: function (json) {
            }
        })
    }

}