<template>
    <main class="editing">
        <v-container>
            <div class="admin-table">
                <!-- Search input for searching by last name -->
                <v-text-field
                    v-model="lastNameSearch"
                    label="Search by Last Name"
                    class="mx-4"
                ></v-text-field>

                <v-data-table
                    :headers="headers"
                    :items="filteredUsers"
                    item-key="User_id"
                    class="elevation-1"
                    :search="search"
                    :sort-by="['id']"
                >
                    <template v-slot:item.action="{ item }">
                        <!-- Render the button only for users with roles Moderator or User -->
                        <v-btn
                            v-if="isModeratorOrUser(item.role)"
                            @click="changeUserRole(item.id, item.role)"
                            >Change Role</v-btn
                        >
                    </template>
                </v-data-table>
            </div>
        </v-container>
    </main>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            search: '',
            lastNameSearch: '', // New data property for searching by last name
            users: [],
            headers: [
                { text: 'User ID', value: 'id' },
                { text: 'First Name', value: 'first_name' },
                { text: 'Last Name', value: 'last_name' },
                { text: 'Email', value: 'email' },
                { text: 'Role ID', value: 'role' },
                { text: 'Role Name', value: 'role_name' }, // New column for role names
                { text: 'Action', value: 'action', sortable: false },
            ],
        };
    },
    mounted() {
        this.getAllUsers();
    },
    computed: {
        // Map role IDs to role names
        roleNames() {
            return {
                1: 'User',
                2: 'Moderator',
                3: 'Admin',
            };
        },
        filteredUsers() {
            if (!this.lastNameSearch) return this.users; // Return all users if no search input provided
            const searchUpperCase = this.lastNameSearch.toUpperCase();
            return this.users.filter((user) =>
                user.last_name.toUpperCase().includes(searchUpperCase)
            );
        },
    },
    methods: {
        async getAllUsers() {
            try {
                const response = await axios.get(
                    'http://18.206.186.97:8000/getAllUsers'
                );
                // Map role IDs to role names for each user
                this.users = response.data.map((user) => ({
                    ...user,
                    role_name: this.roleNames[user.role], // Add role_name property
                }));
            } catch (error) {
                console.error('Error fetching users:', error);
            }
        },
        async changeUserRole(userId, roleId) {
            try {
                // Determine the new role ID based on the current role ID
                const newRoleId = roleId === 1 ? 2 : 1;
                await axios.put('http://18.206.186.97:8000/changeRole', {
                    id: userId,
                    role_id: newRoleId,
                });
                // Refresh the user list after role change
                this.getAllUsers();
            } catch (error) {
                console.error('Error changing user role:', error);
            }
        },
        isModeratorOrUser(roleId) {
            // Check if the role ID is either for Moderator or User
            return roleId === 2 || roleId === 1;
        },
    },
};
</script>
