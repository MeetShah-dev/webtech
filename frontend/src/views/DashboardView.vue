<script>
import axios from 'axios'
export default {
    components: {
        NavBar: () => import('@/components/NavBar.vue'),
        SideBar: () => import('@/components/SideBar.vue'),
    },
    name: 'DashboardComponent',
    data() {
        return {
            userData: null,
            responseData: null,
        };
    },
    mounted(){ 
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        }); 

    },
    beforeRouteEnter(to, from, next) {
        const urlParams = new URLSearchParams(window.location.search);
        const userFromUrl = urlParams.get('user');

        let userData = null;

        if (userFromUrl) {
            try {
                userData = JSON.parse(decodeURIComponent(userFromUrl));
                sessionStorage.setItem('user', JSON.stringify(userData)); 
            } catch (error) {
                console.error('Failed to parse user data from URL:', error);
                next('/login'); 
                return;
            }
        } else {
            const userFromSession = sessionStorage.getItem('user');
            if (userFromSession) {
                try {
                    userData = JSON.parse(userFromSession);
                } catch (error) {
                    console.error(
                        'Failed to parse user data from sessionStorage:',
                        error
                    );
                    next('/login'); 
                    return;
                }
            }
        }
        if (userData) {
            next((vm) => {
                vm.userData = userData;
                vm.fetchData(); 
            });
        } else {
            next('/login');
        }
    },

    methods: {
        fetchData() {
            const headers = {
                Accept: 'application/json',
                Authorization: `Bearer ${sessionStorage.getItem('token')}`,
            };

            axios
                .get('http://localhost:8083/getAllCategories', { headers })
                .then((response) => {
                    this.responseData = response.data;
                })
                .catch((error) => {
                    console.error('Error fetching data:', error);
                });
        },
    },
};
</script>

<template>
    <div class="main">
        <nav-bar></nav-bar>
        <main class="editing">
            <side-bar :role="userData.role_id"></side-bar>
        </main>
    </div>
</template>

<style scoped>
.editing {
    margin-right: 0px;
    padding: 10px;
    display: flex;
    height: 800px;
    justify-content: space-between;
}

.main-container {
    padding: 10px;
    height: max-content;
}

.main-container-btn {
    display: flex;
    justify-content: space-between;
}
.side-container {
    padding: 0;
    width: 30%;
    height: 100%;
    background-color: #c1e2f4;
}
</style>
