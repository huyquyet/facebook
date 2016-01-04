/**
 * Created by FRAMGIA\nguyen.huy.quyet on 28/12/2015.
 */

//  loai bo khoang trang dau va cuoi String
function Trim(sString) {
    while (sString.substring(0, 1) == ' ') {
        sString = sString.substring(1, sString.length);
    }
    while (sString.substring(sString.length - 1, sString.length) == ' ') {
        sString = sString.substring(0, sString.length - 1);
    }
    return sString;
}


function display_none_btn(id) {
    $('#id_btn_' + id + '_edit_comment').css('display', 'block');
    $('#id_btn_' + id + '_delete_comment').css('display', 'block');
    $('#id_btn_' + id + '_update_comment').css('display', 'none');
    $('#id_btn_' + id + '_cancel_comment').css('display', 'none');
}
function display_none_content(id) {
    $('#view_comment_content_data_' + id).css('display', 'block');
    $('#view_comment_content_form_data_edit_' + id).css('display', 'none');
}
function display_block_btn(id) {
    $('#id_btn_' + id + '_edit_comment').css('display', 'none');
    $('#id_btn_' + id + '_delete_comment').css('display', 'none');
    $('#id_btn_' + id + '_update_comment').css('display', 'block');
    $('#id_btn_' + id + '_cancel_comment').css('display', 'block');
}
function display_block_content(id) {
    $('#view_comment_content_data_' + id).css('display', 'none');
    $('#view_comment_content_form_data_edit_' + id).css('display', 'block');
}