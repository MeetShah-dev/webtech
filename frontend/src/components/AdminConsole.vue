<script>
export default {
    data() {
        return {
            search: '',
            newUser: {
                User_id: '',
                Role_id: '',
                Is_moderator: false,
            },
            users: [
                {
                    User_id: 1,
                    Role_id: 101,
                    Is_moderator: true,
                },
                {
                    User_id: 2,
                    Role_id: 102,
                    Is_moderator: false,
                },
                // Add more users as needed
            ],
        };
    },
    computed: {
        headers() {
            return [
                { text: 'User_id', value: 'User_id' },
                { text: 'Role_id', value: 'Role_id' },
                {
                    text: 'Is Moderator',
                    value: 'Is_moderator',
                    align: 'center',
                },
            ];
        },
    },
    methods: {
        filterAllValues(users, search) {
            // Convert search to uppercase for case-insensitive comparison
            const searchUpperCase = search.toUpperCase();

            // Iterate over each property in the item
            for (const User_id in users) {
                if (Object.prototype.hasOwnProperty.call(users, User_id)) {
                    const value = users[User_id];

                    // Check if the value is a string and matches the search criteria
                    if (
                        typeof value === 'string' &&
                        value.toUpperCase().includes(searchUpperCase)
                    ) {
                        return true; // Return true if any property matches the search
                    }
                }
            }

            return false; // Return false if no property matches the search
        },
    },
};
</script>

<template>
    <main class="editing">
        <v-container>
            <div class="admin-table">
                <v-data-table
                    :headers="headers"
                    :items="users"
                    item-key="User_id"
                    class="elevation-1"
                    :search="search"
                    :custom-filter="filterAllValues"
                >
                    <template v-slot:top>
                        <v-text-field
                            v-model="search"
                            label="Search (Case-insensitive)"
                            class="mx-4"
                        ></v-text-field>
                    </template>
                    <template v-slot:body.append>
                        <tr>
                            <td></td>
                            <td>
                                <v-text-field
                                    v-model="newUser.User_id"
                                    type="number"
                                    label="User_id"
                                ></v-text-field>
                            </td>
                            <td>
                                <v-text-field
                                    v-model="newUser.Role_id"
                                    type="number"
                                    label="Role_id"
                                ></v-text-field>
                            </td>
                            <td>
                                <v-checkbox
                                    v-model="newUser.Is_moderator"
                                    label="Is Moderator"
                                    hide-details
                                ></v-checkbox>
                            </td>
                            <td>
                                <v-row>
                                    <v-btn v-model="newUser.Add_user"
                                        >Add User</v-btn
                                    >
                                </v-row>
                            </td>
                        </tr>
                    </template>
                </v-data-table>
            </div>
        </v-container>
    </main>
</template>
<style></style>
