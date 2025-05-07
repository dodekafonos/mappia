<template>
    <button class="recenter-btn" @click="$emit('recenter')">
      📍 Recentralizar
    </button>
  </template>
  
  <style scoped>
  .recenter-btn {
    /* position: absolute; */
    bottom: 1.5rem;
    right: 1.5rem;
    z-index: 1000;
    background-color: #2563eb;
    color: white;
    border: none;
    border-radius: 0.5rem;
    padding: 0.5rem 1rem;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: background-color 0.2s;
  }
  .recenter-btn:hover {
    background-color: #1d4ed8;
  }
  </style>
  