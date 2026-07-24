<template>
  <div class="space-y-6">
    <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
      <h1 class="text-3xl font-bold">Biblioteca de Scripts</h1>
      <input
        v-model="search"
        type="text"
        placeholder="Buscar scripts..."
        class="w-full sm:w-64 px-4 py-2 bg-slate-800 border border-slate-700 rounded-lg focus:outline-none focus:border-blue-500 transition"
      />
    </div>

    <!-- Filter -->
    <div class="flex gap-2 flex-wrap">
      <button
        v-for="cat in categories"
        :key="cat"
        @click="toggleCategory(cat)"
        :class="{
          'bg-blue-600 text-white': selectedCategories.includes(cat),
          'bg-slate-800 text-slate-300 hover:bg-slate-700': !selectedCategories.includes(cat)
        }"
        class="px-4 py-2 rounded-lg transition"
      >
        {{ cat }}
      </button>
    </div>

    <!-- Scripts Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div
        v-for="script in filteredScripts"
        :key="script.id"
        @click="navigateTo(script.id)"
        class="bg-slate-800/50 border border-slate-700 hover:border-blue-500 rounded-lg p-6 cursor-pointer transition hover:bg-slate-800/80 hover:shadow-lg hover:shadow-blue-500/20"
      >
        <div class="flex justify-between items-start mb-3">
          <h3 class="text-lg font-semibold text-blue-300 flex-1">{{ script.name }}</h3>
          <span class="px-2 py-1 text-xs bg-slate-700 rounded ml-2 whitespace-nowrap">{{ script.type }}</span>
        </div>
        <p class="text-slate-400 text-sm mb-4 line-clamp-2">{{ script.description }}</p>
        <div class="flex justify-between items-center text-xs text-slate-500">
          <span class="text-slate-500">{{ script.category }}</span>
          <span class="text-yellow-400">⭐ {{ script.rating }}</span>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-if="filteredScripts.length === 0" class="text-center py-12">
      <p class="text-slate-400">Nenhum script encontrado. Tente ajustar seus filtros.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const search = ref('')
const selectedCategories = ref([])

const categories = ref([
  'Active Directory', 'Exchange', 'SQL Server', 'Windows Server',
  'Hyper-V', 'Backup', 'Network', 'Security'
])

const scripts = ref([
  { id: 1, name: 'Get User Mailbox Size', type: 'PowerShell', category: 'Exchange', description: 'Obtém o tamanho da caixa de correio de um usuário', rating: 4.8 },
  { id: 2, name: 'Bulk Reset AD Password', type: 'PowerShell', category: 'Active Directory', description: 'Reseta senhas em massa no Active Directory', rating: 4.9 },
  { id: 3, name: 'Backup SQL Database', type: 'PowerShell', category: 'SQL Server', description: 'Faz backup automático de banco de dados SQL', rating: 4.7 },
  { id: 4, name: 'Monitor VM Performance', type: 'PowerShell', category: 'Hyper-V', description: 'Monitora performance de máquinas virtuais', rating: 4.6 },
  { id: 5, name: 'List AD Users', type: 'PowerShell', category: 'Active Directory', description: 'Lista todos os usuários do Active Directory com filtros', rating: 4.5 },
  { id: 6, name: 'Enable BitLocker', type: 'PowerShell', category: 'Security', description: 'Ativa BitLocker em máquinas Windows Server', rating: 4.8 },
  { id: 7, name: 'Check Disk Space', type: 'Batch', category: 'Windows Server', description: 'Verifica espaço em disco dos servidores', rating: 4.4 },
  { id: 8, name: 'Export Exchange Mailbox', type: 'PowerShell', category: 'Exchange', description: 'Exporta caixa de correio do Exchange para arquivo', rating: 4.7 },
])

const toggleCategory = (category) => {
  const index = selectedCategories.value.indexOf(category)
  if (index > -1) {
    selectedCategories.value.splice(index, 1)
  } else {
    selectedCategories.value.push(category)
  }
}

const filteredScripts = computed(() => {
  return scripts.value.filter(script => {
    const matchesSearch = script.name.toLowerCase().includes(search.value.toLowerCase()) ||
                         script.description.toLowerCase().includes(search.value.toLowerCase())
    const matchesCategory = selectedCategories.value.length === 0 || selectedCategories.value.includes(script.category)
    return matchesSearch && matchesCategory
  })
})

const navigateTo = (id) => {
  router.push(`/scripts/${id}`)
}
</script>
