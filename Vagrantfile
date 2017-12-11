# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure('2') do |config|

  config.vm.box = 'azure'
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box' #Caja base vacía
  config.vm.network "public_network" 
  config.vm.network "forwarded_port", guest: 80, host: 80

  # use local ssh key to connect to remote vagrant box
  config.vm.provider :azure do |azure, override|
    config.ssh.private_key_path = '~/.ssh/id_rsa'
    azure.vm_image_urn = 'canonical:UbuntuServer:16.04-LTS:16.04.201701130' #Imagen base del sistema
    azure.vm_size = 'Basic_A0' #Tamaño (recursos) de la MV
    azure.location = 'westeurope'
    azure.tcp_endpoints = '80'
    azure.vm_name = "maquinaiv"
    azure.resource_group_name= "proyecto"
    azure.tenant_id = '9103da1f-804e-4044-9a3b-e60990b9813f'
    azure.client_id = 'eb307949-b71b-4f87-8874-a1e208cdbb04'
    azure.client_secret = 'zSzScVYui9CSKmkX6GvNNBU6jgyYxYKK70nZ8Zwx/vw='
    azure.subscription_id = '98df0dfe-7115-48e6-875e-98527affc7d7'
  end



  # Provisionar con ansible
  config.vm.provision "ansible" do |ansible|
    ansible.sudo = true
    ansible.playbook = "playbook.yml"
    ansible.verbose = "-vvvv"

    ansible.host_key_checking = false
  end

end
