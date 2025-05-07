<template>
    <Drawer
      :visible="visible"
      position="right"
      header="Novo Evento"
      class="!w-full md:!w-80 lg:!w-[30rem]"
      @update:visible="$emit('update:visible', $event)"
    >
      <form class="flex flex-col gap-4 p-2" @submit.prevent="submitForm">
        <div class="flex flex-col">
          <label class="font-medium mb-1">Nome do evento</label>
          <InputText v-model="form.name" placeholder="Digite o nome do evento" />
        </div>
  
        <div class="flex flex-col">
          <label class="font-medium mb-1">Início</label>
          <Calendar
            v-model="form.start"
            showTime
            hourFormat="24"
            placeholder="Selecione data e hora"
          />
        </div>
  
        <div class="flex flex-col">
          <label class="font-medium mb-1">Término</label>
          <Calendar
            v-model="form.end"
            showTime
            hourFormat="24"
            placeholder="Selecione data e hora"
          />
        </div>
  
        <div class="flex flex-col">
          <label class="font-medium mb-1">Categoria</label>
          <Dropdown
            v-model="form.category"
            :options="categories"
            optionLabel="label"
            placeholder="Selecione uma categoria"
          />
        </div>
  
        <div class="flex flex-col">
          <label class="font-medium mb-1">Descrição</label>
          <Textarea v-model="form.description" rows="3" placeholder="Descrição opcional..." />
        </div>
  
        <Button type="submit" label="Salvar evento" class="mt-4 w-full" />
      </form>
    </Drawer>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import Drawer from 'primevue/drawer'
  import InputText from 'primevue/inputtext'
  import Calendar from 'primevue/calendar'
  import Dropdown from 'primevue/dropdown'
  import Textarea from 'primevue/textarea'
  import Button from 'primevue/button'
  
  defineProps(['visible'])
  defineEmits(['update:visible'])
  
  const form = ref({
    name: '',
    start: null,
    end: null,
    category: null,
    description: '',
  })
  
  const categories = [
    { label: 'Cultura', value: 'cultura' },
    { label: 'Esporte', value: 'esporte' },
    { label: 'Educação', value: 'educacao' },
    { label: 'Protesto', value: 'protesto' },
    { label: 'Outros', value: 'outros' },
  ]
  
  const submitForm = () => {
    console.log('Dados do evento:', form.value)
    // Aqui você pode emitir um evento para salvar ou fechar
  }
  </script>
  
  <style scoped>
  label {
    font-size: 0.875rem;
  }
  </style>
  