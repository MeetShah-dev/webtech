<script>
import axios from 'axios';
import SideBar from '@/components/SideBar.vue'; // Ensure correct import

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
  beforeRouteEnter(to, from, next) {
  // First, attempt to get user data from URL parameters
  const urlParams = new URLSearchParams(window.location.search);
  const userFromUrl = urlParams.get('user');

  let userData = null;

  if (userFromUrl) {
    try {
      // Try parsing the user data from the URL
      userData = JSON.parse(decodeURIComponent(userFromUrl));
      sessionStorage.setItem('user', JSON.stringify(userData));  // Save to sessionStorage
    } catch (error) {
      console.error('Failed to parse user data from URL:', error);
      next('/login');  // Redirect to login if parsing fails
      return;
    }
  } else {
    // If not found in URL, try fetching from sessionStorage
    const userFromSession = sessionStorage.getItem('user');
    if (userFromSession) {
      try {
        userData = JSON.parse(userFromSession);
      } catch (error) {
        console.error('Failed to parse user data from sessionStorage:', error);
        next('/login');  // Redirect to login if parsing fails
        return;
      }
    }
  }
  // Proceed to the route if userData is found; otherwise, redirect to login
  if (userData) {
    next(vm => {
      vm.userData = userData;
      vm.fetchData();  // Assume fetchData exists and properly fetches other necessary data
    });
  } else {
    next('/login');  // Redirect to login if no user data is available
  }
},

  methods: {
    fetchData() {
      const headers = {
        'Accept': 'application/json',
        'Authorization': `Bearer ${sessionStorage.getItem('token')}`
      };

      axios.get('http://localhost:8083/getAllCategories', { headers })
        .then(response => {
          this.responseData = response.data;
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    }
  }
};
</script>

<template>
    <div class="main">
        <nav-bar></nav-bar>
        <h1>Dashboard</h1>
        <main class="editing">
            <side-bar :role="userData.role_id"></side-bar>
            <!-- <div class="main-container"></div> -->
        </main>
    </div>
</template>

<style scoped>
.main {
    margin-left: 350px;
    width: 1500px;
}

.editing {
    margin-right: 0px;
    padding: 10px;
    display: flex;
    height: 800px;
    justify-content: space-between;
}

.main-container {
    /* margin: 10px; */
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
