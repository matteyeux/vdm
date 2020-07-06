
/**
* Theme: Zircos - Bootstrap 4 Admin Dashboard
* Author: Coderthemes
 * Email: coderthemes@gmail.com
* Property Add
*/

$(document).ready(function(){

	$('.dropify').dropify({
        messages: {
            'default': 'Drag and drop a file here or click',
            'replace': 'Drag and drop or click to replace',
            'remove': 'Remove',
            'error': 'Ooops, something wrong appended.'
        },
        error: {
            'fileSize': 'The file size is too big (1M max).'
        }
    });
});