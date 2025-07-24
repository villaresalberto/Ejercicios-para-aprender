#!/usr/bin/env python3
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def mostrar_info(self):
        print (f"[+] Titular: {self.titular}, Saldo disponible: {self.saldo} €")
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"[+] Se ha depositado {cantidad} € en el Titular: {self.titular}. Tu saldo ahora es de: {self.saldo} €")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"[+] Se ha retirado {cantidad} € en el Titular: {self.titular}. Tu saldo ahora es de: {self.saldo} €")
        else:
            print(f"[+] Fondos insuficientes")

    def transferir(self, destino, cantidad):
       if cantidad <= self.saldo:
            self.saldo -= cantidad
            destino.saldo += cantidad
            print(f"{self.titular} ha transferido {cantidad} € a {destino.titular}")
            print(f"{self.titular} → Saldo: {self.saldo} €")
            print(f"{destino.titular} → Saldo: {destino.saldo} €")
       else:
            print(f"{self.titular}: Saldo insuficiente para transferir {cantidad} €") 

cuenta_1 = CuentaBancaria("Alberto", 987)
cuenta_2 = CuentaBancaria("Benito", 1600)
cuenta_3 = CuentaBancaria("Paco", 452)

cuenta_1.mostrar_info()
cuenta_2.mostrar_info()
cuenta_3.mostrar_info()

cuenta_1.depositar(200)
cuenta_1.retirar(1500)
cuenta_1.retirar(450)

cuenta_1.transferir(cuenta_2, 500)
cuenta_2.transferir(cuenta_3, 7500)
cuenta_2.transferir(cuenta_3, 750)
