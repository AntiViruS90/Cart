window.onload = function(){

    document.getElementById('order_button').onclick=function(e){
        e.preventDefault()
        document.getElementById('form').hidden = false
    }
    document.getElementById('btn_order').onclick=function() {
        address = document.getElementById('address').value
        name = document.getElementById('name').value
        tel = document.getElementById('tel').value
        if (address&&name&&tel) {
            let url = '/cart/order/'
            $.ajax(url, {
                method: 'POST',
                data: {
                    address: address,
                    name: name,
                    tel: tel,
                },
                success: function (response) {
                    console.log(response)
                    // window.location.href = '../' # Вариант 1
                    window.location.href = response.link
                },
                error: function (response) {
                    console.log(response)
                }
            })
        } else {
            alert('Please enter valid information')
        }
    }










}
















