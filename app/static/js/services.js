const API_ENDPOINT = 'http://localhost:5000/api';

//  Admin Services

const adminService = {
    queryAdmin() {
        return $.ajax({
            url: `${API_ENDPOINT}/admins`,
            method: 'GET',
            headers: {
                'Accept': 'application/json',
            }
        });
    },

    createAdmin(data) {
        console.log(data);
        return $.ajax({
            url: `${API_ENDPOINT}/admins`,
            method: 'POST',
            data: data,
            headers: {
                // 'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded',
            }
        });
    },

    removeAdmin(id) {
        return $.ajax({
            url: `${API_ENDPOINT}/admins/${id}`,
            method: 'DELETE',
            headers: {
                'Accept': 'application/json'
            }
        });
    },

    getAdmin(id) {
        return $.ajax({
            url: `${API_ENDPOINT}/admins/${id}`,
            method: 'GET',
            headers: {
                'Accept': 'application/json'
            }
        });
    },

    updateAdmin(id, data) {

        return $.ajax({
            url: `${API_ENDPOINT}/admins/${id}`,
            method: 'PUT',
            data: data,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded',
            }
        });
    }

}