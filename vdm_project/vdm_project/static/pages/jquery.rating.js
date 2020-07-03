
/**
* Theme: Zircos - Bootstrap 4 Admin Dashboard
* Author: Coderthemes
* Ratings
*/

;(function ($) {
    $(function () {
        $('#default').raty({
            starOff: 'far fa-star text-muted',
            starOn: 'fas fa-star text-warning'
        });

        $('#score').raty({
            score: 3,
            starOff: 'far fa-star text-muted',
            starOn: 'fas fa-star text-danger'
        });

        $('#score-callback').raty({
            score: function () {
                return $(this).attr('data-score');
            }
        });

        $('#scoreName').raty({
            scoreName: 'entity[score]',
            starOff: 'far fa-star text-muted',
            starOn: 'fas fa-star text-warning'
        });

        $('#number').raty({
            number: 10,
            starOff: 'far fa-star text-muted',
            starOn: 'fas fa-star text-danger'
        });

        $('#number-callback').raty({
            number: function () {
                return $(this).attr('data-number');
            }
        });

        $('#numberMax').raty({
            numberMax: 5,
            number: 100,
            starOff: 'far fa-star text-muted',
            starOn: 'fas fa-star text-purple'
        });

        $('#readOnly').raty({
            readOnly: true,
            score: 3,
            starOff: 'far fa-star text-muted',
            starOn: 'fas fa-star text-success'
        });

        $('#readOnly-callback').raty({
            readOnly: function () {
                return 'true becomes readOnly' == 'true becomes readOnly';
            }
        });

        $('#noRatedMsg').raty({
            readOnly: true,
            noRatedMsg: "I'am readOnly and I haven't rated yet!",
            starOff: 'far fa-star text-muted',
            starOn: 'fas fa-star text-danger'
        });

        $('#halfShow-true').raty({
            score: 3.26
        });

        $('#halfShow-false').raty({
            halfShow: false,
            score: 3.26,
            starOff: 'far fa-star text-muted',
            starOn: 'fas fa-star text-danger'
        });

        $('#round').raty({
            round: {down: .26, full: .6, up: .76},
            score: 3.26,
            starOff: 'far fa-star text-muted',
            starOn: 'fas fa-star text-pink'
        });

        $('#half').raty({
            half: true
        });

        $('#starHalf').raty({
            half: true,
            starHalf: 'fas fa-star-half text-danger',
            starOff: 'far fa-star text-muted',
            starOn: 'fas fa-star text-danger'
        });

        $('#click').raty({
            click: function (score, evt) {
                alert('ID: ' + $(this).attr('id') + "\nscore: " + score + "\nevent: " + evt.type);
            }
        });

        $('#hints').raty({hints: ['a', null, '', undefined, '*_*']});

        $('#star-off-and-star-on').raty({
            starOff: 'far fa-bell text-muted',
            starOn: 'fas fa-bell text-custom'
        });

        $('#cancel').raty({
            cancel: true,
            starOff: 'far fa-star text-muted',
            starOn: 'fas fa-star text-danger'
        });

        $('#cancelHint').raty({
            cancel: true,
            cancelHint: 'My cancel hint!',
            starOff: 'far fa-star text-muted',
            starOn: 'fas fa-star text-success'
        });

        $('#cancelPlace').raty({
            cancel: true,
            cancelPlace: 'right',
            starOff: 'far fa-star text-muted',
            starOn: 'far fa-star text-purple'
        });

        $('#cancel-off-and-cancel-on').raty({
            cancel: true,
            cancelOff: 'far fa-minus-square text-muted',
            cancelOn: 'fas fa-minus-square text-danger'
        });

        $('#iconRange').raty({
            iconRange: [
                {range: 1, on: 'fas fa-cloud', off: 'far fa-circle'},
                {range: 2, on: 'fas fa-cloud-download-alt', off: 'far fa-circle'},
                {range: 3, on: 'fas fa-cloud-upload-alt', off: 'far fa-circle'},
                {range: 4, on: 'fas fa-circle', off: 'far fa-circle'},
                {range: 5, on: 'fas fa-cogs', off: 'far fa-circle'}
            ]
        });

        $('#size-md').raty({
            cancel: true,
            half: true
        });

        $('#size-lg').raty({
            cancel: true,
            half: true
        });

        $('#target-div').raty({
            cancel: true,
            target: '#target-div-hint',
            starOff: 'far fa-star text-muted',
            starOn: 'fas fa-star text-custom'
        });

        $('#targetType').raty({
            cancel: true,
            target: '#targetType-hint',
            targetType: 'score',
            starOff: 'far fa-star text-muted',
            starOn: 'fas fa-star text-warning'
        });

        $('#targetFormat').raty({
            target: '#targetFormat-hint',
            targetFormat: 'Rating: {score}',
            starOff: 'far fa-star text-muted',
            starOn: 'fas fa-star text-danger'
        });

        $('#mouseover').raty({
            mouseover: function (score, evt) {
                alert('ID: ' + $(this).attr('id') + "\nscore: " + score + "\nevent: " + evt.type);
            }
        });

        $('#mouseout').raty({
            width: 150,
            mouseout: function (score, evt) {
                alert('ID: ' + $(this).attr('id') + "\nscore: " + score + "\nevent: " + evt.type);
            }
        });
    });
})(jQuery);