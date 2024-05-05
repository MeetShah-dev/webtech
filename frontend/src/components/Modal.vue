<template>
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <p>{{ message }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        showModal: true,
      };
    },
    props: {
        message: String
    },
    mounted() {
      this.$root.$on('show-modal', (message) => {
        this.message = message;
        this.showModal = true;
      });
    },
    methods: {
      closeModal() {
        this.showModal = false;
      }
    }
  };
  </script>
  
  <style>
  .modal {
    display: inline; 
    position: fixed; 
    z-index: 999; 
    left: 0;
    top: 0;
    width: 100%;
    height: 100%; 
    overflow: auto; 
    background-color: rgba(0,0,0,0.4); 
  }
  
  .modal-content {
    background-color: #fefefe;
    margin: 15% auto; 
    padding: 20px;
    border: 1px solid #888;
    width: 60%; 
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
  }
  
  .close {
    color: #ca3333;
    float: right;
    font-size: 28px;
    font-weight: bold;
  }
  
  .close:hover,
  .close:focus {
    color: rgb(232, 115, 115);
    text-decoration: none;
    cursor: pointer;
  }
  </style>
  