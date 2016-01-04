/**
 * Created by FRAMGIA\nguyen.huy.quyet on 04/01/2016.
 */

function create_post_comment(post_id) {
    var values = $('#create_comment_post_' + post_id + '_content');
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
                $('#view_comments_post_' + post_id).append(json.html);
            },
            error: function (json) {
                alert('Error submit data')
            }
        });
    }
}

function like_comment(comment_id) {
    $.ajax({
        url: 'like/comment/like',
        type: 'POST',
        data: {
            comment_id: comment_id
        },
        success: function (json) {
            $('#view_comment_content_like_' + comment_id).html('<button type="button"' +
                'class="btn btn-link btn-xs text" onclick="unlike_comment(' + comment_id + ')">Unlike ');
            $('#view_comment_content_like_number_' + comment_id).css('display', 'block');
            $('#number_like_comment_' + comment_id).html(json.total_like_comment);
        }
        ,
        error: function (json) {
            alert('Error submit data')
        }
    });
}

function unlike_comment(comment_id) {
    $.ajax({
        url: 'like/comment/unlike',
        type: 'POST',
        data: {
            comment_id: comment_id
        },
        success: function (json) {
            $('#view_comment_content_like_' + comment_id).html('<button type="button"' +
                'class="btn btn-link btn-xs text" onclick="like_comment(' + comment_id + ')">Like ');
            if (json.total_like_comment > 0) {
                $('#view_comment_content_like_number_' + comment_id).css('display', 'block');
                $('#number_like_comment_' + comment_id).html(json.total_like_comment);
            } else {
                $('#view_comment_content_like_number_' + comment_id).css('display', 'none');
            }

        }
        ,
        error: function (json) {
            alert('Error submit data')
        }
    });
}

function confirm_delete_post_comment(comment_id) {
    var result = confirm('Are you sure you want delete comment ?');
    if (result) {
        delete_post_comment(comment_id);
    }
}

function delete_post_comment(comment_id) {
    $.ajax({
        url: 'comment/delete/post',
        type: 'POST',
        data: {
            comment_id: comment_id
        },
        success: function (json) {
            alert('Success submit data');
            $('#view_comment_post_' + comment_id).hide();
        },
        error: function (json) {
            alert('Error submit data')
        }
    });
}

function update_post_comment(comment_id) {

    var values = $('#view_comment_content_data_edit_' + comment_id);
    var content_comment = Trim(values.val());
    if (content_comment == '') {
        return false
    } else {
        $.ajax({
            url: 'comment/edit/post',
            type: 'POST',
            data: {
                comment_id: comment_id,
                content_comment: content_comment
            },
            success: function (json) {
                $('#view_comment_content_data_' + comment_id).html(json.data);
                display_none_btn(comment_id);
                display_none_content(comment_id);
            },
            error: function (json) {
                alert('Error submit data')
            }
        });
    }
}

function load_more_comment(post_id, start, end, number_comment) {
    var end_start = end;
    var end_end = end + (end - start);
    $.ajax({
        url: '/comment/load_more_comment/',
        type: 'POST',
        data: {
            post_id: post_id,
            start: start,
            end: end,
            number_comment: number_comment
        },
        success: function (json) {
            var data = json.data;
            for (var i = 0; i < data.length; i++) {
                $('#view_comments_post_' + post_id).prepend(data[i]);
            }
            if (end < number_comment) {
                $('#view_more_comment_' + post_id).html('<button type="button" class="btn btn-link btn-xs pull-left"' +
                    'onclick="load_more_comment(' + post_id + ', ' + end_start + ' ,' + end_end + ',' + number_comment + '">View more comment...</button>');
            }
            else {
                $('#view_more_comment_' + post_id).hide();
            }
        },
        error: function (json) {
            alert('Error');
        }
    });
}