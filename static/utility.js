
function apiCall(url,method,payload){
    method = method || 'GET'
    return new Promise((resolve,reject)=>{
        jQuery.ajax({
            url: url,
            type: method,
            contentType : 'application/json',
            data: payload!==undefined && JSON.stringify(payload),
            success: function (data) {
                resolve(data);
            },
            error: function(err){
                reject(err);
            }
        });
    });
}
function push(){
    const inputElement = document.getElementById('pushInput')
    if(inputElement.value === ""){
        alert("Please Enter the push value");
        return;
    }
    let value = Number(inputElement.value);
    if(Number.isNaN(value)){
        value = inputElement.value;
    }
    inputElement.value = "";
    apiCall('/stack','PUT',{val:value}).then((response)=>{
        if (Object.keys(response).length===0){
            alert("Stack Overflow");
            return;
        }
    })
}
function pop(){
    apiCall('/stack','DELETE');
}
function capacity(){
    let value = document.getElementById('capacityInput').value;
    if (!Number.isInteger(Number(value)) || value === ""){
        alert('please enter integer stack capacity')
        return;
    }
    apiCall('/stack','POST',{capacity:Number(value)}).then((response)=>{
        document.getElementById('stackOps').style.display = "block"
    })
}

function reset(){
    apiCall('/stack?reset=true','DELETE').then((response)=>{
        document.getElementById('stackValuesLabel').innerText = "";
        document.getElementById('pushInput').value = "";
        document.getElementById('capacityInput').value = "";
        document.getElementById('stackOps').style.display = "none";
    })
}
function print(){
    apiCall('/stack?all=true').then((response)=>{
        const inputElement = document.getElementById('stackValuesLabel');
        inputElement.innerText = response.join(", ");
    })
}
function onPageLoad(){
    document.getElementById('stackOps').style.display = "none";
    apiCall('/stack?capacity=true').then((response)=>{
        if(response.val !== undefined){
            document.getElementById('capacityInput').value = response.val;
            document.getElementById('stackOps').style.display = "block";
            print()
        }
    })
}