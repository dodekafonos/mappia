<template>
    <div
      v-if="position"
      class="absolute z-[1000] transform -translate-x-1/2 -translate-y-full cursor-pointer"
      :style="{ left: `${position.x}px`, top: `${position.y}px` }"
      @click="$emit('click')"
      title="Criar novo evento"
    >
      <div
        class="w-10 h-10 rounded-full bg-blue-600 hover:bg-blue-700 text-white flex items-center justify-center shadow-lg transition-all"
      >
        +
      </div>
    </div>
  </template>
  
  <script setup>
  defineProps({
    position: {
      type: Object,
      required: false, // permitir que ele não exista no início
    },
  })
  
  defineEmits(['click'])
  </script>
  