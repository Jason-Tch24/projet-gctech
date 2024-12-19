<template>
    <div class="activity-card">
      <img :src="activity.image" alt="Activity Image" class="activity-image" />
      <div class="activity-content">
        <p class="category">{{ activity.category }}</p>
        <h3 class="title">{{ activity.title }}</h3>
        <p class="location">{{ activity.location }}</p>
        <button class="reserve-btn">Réserver</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      activity: {
        type: Object,
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>
  .activity-card {
    border: 1px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
  }
  .activity-image {
    width: 100%;
    height: 150px;
    object-fit: cover;
  }
  .activity-content {
    padding: 16px;
  }
  .category {
    color: #7b7b7b;
    font-size: 14px;
    margin-bottom: 8px;
  }
  .title {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 8px;
  }
  .location {
    color: #7b7b7b;
    font-size: 14px;
    margin-bottom: 16px;
  }
  .reserve-btn {
    background-color: #6200ea;
    color: white;
    padding: 10px 16px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  .reserve-btn:hover {
    background-color: #4b00b8;
  }
  </style>
  