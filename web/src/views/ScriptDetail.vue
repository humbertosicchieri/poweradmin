<template>
  <div class="space-y-6">
    <router-link to="/scripts" class="text-blue-400 hover:text-blue-300 inline-flex items-center gap-2 transition">
      ← Voltar
    </router-link>

    <div class="bg-slate-800/50 border border-slate-700 rounded-lg p-8 space-y-8">
      <!-- Header -->
      <div class="space-y-4">
        <div class="flex justify-between items-start gap-4">
          <div class="flex-1">
            <h1 class="text-4xl font-bold mb-2">{{ script.name }}</h1>
            <p class="text-slate-400">{{ script.description }}</p>
          </div>
          <span class="px-4 py-2 bg-slate-700 rounded-lg whitespace-nowrap">{{ script.type }}</span>
        </div>
      </div>

      <!-- Metadata -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 py-6 border-y border-slate-700">
        <div>
          <div class="text-slate-400 text-sm">Categoria</div>
          <div class="font-semibold">{{ script.category }}</div>
        </div>
        <div>
          <div class="text-slate-400 text-sm">Avaliação</div>
          <div class="font-semibold text-yellow-400">⭐ {{ script.rating }}</div>
        </div>
        <div>
          <div class="text-slate-400 text-sm">Última Atualização</div>
          <div class="font-semibold">{{ script.updated }}</div>
        </div>
        <div>
          <div class="text-slate-400 text-sm">Downloads</div>
          <div class="font-semibold">{{ script.downloads }}</div>
        </div>
      </div>

      <!-- Code Section -->
      <div class="space-y-4">
        <h2 class="text-2xl font-bold">Código</h2>
        <div class="bg-slate-900 border border-slate-700 rounded-lg overflow-hidden">
          <pre class="p-4 overflow-x-auto"><code class="language-powershell">{{ script.code }}</code></pre>
        </div>
        <button @click="copyCode" class="px-4 py-2 bg-slate-700 hover:bg-slate-600 rounded-lg transition text-sm">
          {{ copied ? '✓ Copiado' : '📋 Copiar Código' }}
        </button>
      </div>

      <!-- Usage Section -->
      <div class="space-y-4">
        <h2 class="text-2xl font-bold">Instruções de Uso</h2>
        <div class="bg-slate-900 border border-slate-700 rounded-lg p-4">
          <p class="text-slate-300 whitespace-pre-line">{{ script.usage }}</p>
        </div>
      </div>

      <!-- Requirements Section -->
      <div class="space-y-4">
        <h2 class="text-2xl font-bold">Requisitos</h2>
        <ul class="list-disc list-inside space-y-2 text-slate-300">
          <li v-for="req in script.requirements" :key="req">{{ req }}</li>
        </ul>
      </div>

      <!-- Actions -->
      <div class="flex flex-col sm:flex-row gap-4 pt-4 border-t border-slate-700">
        <button @click="downloadScript" class="flex-1 px-6 py-3 bg-blue-600 hover:bg-blue-700 rounded-lg font-semibold transition flex items-center justify-center gap-2">
          📥 Baixar Script
        </button>
        <button @click="toggleFavorite" :class="{
          'bg-red-600 hover:bg-red-700': isFavorite,
          'bg-slate-700 hover:bg-slate-600': !isFavorite
        }" class="flex-1 px-6 py-3 rounded-lg font-semibold transition flex items-center justify-center gap-2">
          {{ isFavorite ? '❤️' : '🤍' }} {{ isFavorite ? 'Remover' : 'Favoritar' }}
        </button>
        <button @click="shareScript" class="flex-1 px-6 py-3 bg-slate-700 hover:bg-slate-600 rounded-lg font-semibold transition flex items-center justify-center gap-2">
          🔗 Compartilhar
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const copied = ref(false)
const isFavorite = ref(false)

const script = ref({
  name: 'Get User Mailbox Size',
  description: 'Script para obter o tamanho total da caixa de correio de um usuário no Exchange Online',
  type: 'PowerShell',
  category: 'Exchange',
  rating: 4.8,
  updated: '2024-07-24',
  downloads: 1250,
  code: `# Get Mailbox Size
Connect-ExchangeOnline

$mailbox = Get-Mailbox -Identity "usuario@empresa.com"
$stats = Get-MailboxStatistics -Identity $mailbox.DistinguishedName

Write-Host "Mailbox: $($mailbox.PrimarySmtpAddress)"
Write-Host "Size: $($stats.TotalItemSize)"
Write-Host "Item Count: $($stats.ItemCount)"
Write-Host "Last Logon: $($stats.LastLogonTime)"`,
  usage: `1. Certifique-se de ter permissões de administrador do Exchange
2. Conecte-se ao Exchange Online
3. Substitua "usuario@empresa.com" pelo email do usuário
4. Execute o script no PowerShell ISE ou Terminal
5. O resultado será exibido no console`,
  requirements: [
    'PowerShell 5.1 ou superior',
    'Módulo ExchangeOnlineManagement instalado',
    'Permissões de administrador do Exchange',
    'Conexão com a Internet'
  ]
})

const copyCode = async () => {
  await navigator.clipboard.writeText(script.value.code)
  copied.value = true
  setTimeout(() => {
    copied.value = false
  }, 2000)
}

const downloadScript = () => {
  const element = document.createElement('a')
  element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(script.value.code))
  element.setAttribute('download', `${script.value.name.replace(/\s+/g, '_')}.ps1`)
  element.style.display = 'none'
  document.body.appendChild(element)
  element.click()
  document.body.removeChild(element)
}

const toggleFavorite = () => {
  isFavorite.value = !isFavorite.value
}

const shareScript = () => {
  const url = window.location.href
  navigator.clipboard.writeText(url)
  alert('Link copiado para a área de transferência!')
}
</script>
