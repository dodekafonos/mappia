<template>
  <button
    @click="handleClick"
    class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded shadow"
  >
    Novo evento
  </button>
</template>

<script setup>
const emit = defineEmits(['click'])

function handleClick() {
  emit('click')
}
</script>


<style scoped>
button {
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

button:hover {
  background-color: #1d4ed8;
}
</style>
