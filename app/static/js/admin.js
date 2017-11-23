$(function() {
    const $createAdminModel = $('#create-admin-modal');
    const $adminListTable = $('#admin-list-table');
    const $editAdminModal = $('#edit-admin-modal');

    $createAdminModel
        .find('form')
        .on('submit', openCreateAdmin.bind($createAdminModel));

    $adminListTable.on('click', '.edit-admin-btn', handleAdminEdit.bind($editAdminModal));
    $adminListTable.on('click', '.remove-admin-btn', handleAdminRemove);

    $editAdminModal
        .find('form')
        .on('submit', openEditAdmin.bind($editAdminModal));


    fetchAdminList();
})

function openCreateAdmin(e) {
    e.preventDefault()
    const $modal = this;
    const formData = $modal.find('form').serialize();


    adminService.createAdmin(formData).then(() => {
        $modal.find('form')[0].reset();
        $modal.modal('hide');
        $('#successmodal').modal();
    })
}

function fetchAdminList() {
    adminService
        .queryAdmin()
        .then(function(result) {
            console.log(result)
            $('#admin-list-table').find('tbody').loadTemplate(
                $('#admin-list-item-tpl'), result
            )
        })
}

function handleAdminEdit(e) {
    const $modal = this;
    const adminId = $(e.target).data('id');
    adminService
        .getAdmin(adminId)
        .then((admin) => {
            $modal.find('input').each((i, input) => {
                const field_name = $(input).attr('name');
                $(input).val(admin[field_name]);
            })
        })
}

function openEditAdmin(e) {
    e.preventDefault();
    const $modal = this;
    const formData = $modal.find('form').serialize();
    const adminId = $modal.find("input[name = 'id']").val();

    adminService
        .updateAdmin(adminId, formData)
        .then(() => {
            $modal.modal('hide');
            fetchAdminList();
        });
}

function handleAdminRemove(e) {
    const adminId = $(this).data('id');
    // console.log(usrId);

    adminService
        .removeAdmin(adminId)
        .then(fetchAdminList);
}