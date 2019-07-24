#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2019-07-01 17:23:01
# @Author: xiangsikai
#-----------------------------------------
# Start margin size: 100x100
# The startup script: python3 monitoring.py 
# Close the script: q
# matters need attention: forbid "ctrl + c"
#-----------------------------------------
# ############# debugger ############## #
# from pudb import set_trace;set_trace()#

import queue
import threading
import os
import sys
import psutil
import time
import term
import tty
import termios
import datetime
import platform


class Run(object):
    """Perform each task"""

    def run(self):
        """Enable multithreading to complete tasks"""

        global flag
        flag = True

        thread_get = threading.Thread(
            target=Manage("get").mamage_get)
        thread_cpu = threading.Thread(
            target=Manage("frames_cpu").mamage_put)
        thread_memory = threading.Thread(
            target=Manage("frames_memory").mamage_put)
        thread_swap = threading.Thread(
            target=Manage("frames_swap").mamage_put)
        thread_disk = threading.Thread(
            target=Manage("frames_disk").mamage_put)
        thread_diskio = threading.Thread(
            target=Manage("frames_diskio").mamage_put)
        thread_system = threading.Thread(
            target=Manage("frames_system").mamage_put)
        thread_network = threading.Thread(
            target=Manage("frames_network").mamage_put)
        thread_version = threading.Thread(
            target=Manage("frames_version").mamage_put)
        thread_process = threading.Thread(
            target=Manage("frames_process").mamage_put)

        thread_process.start()
        thread_cpu.start()
        thread_memory.start()
        thread_swap.start()
        thread_disk.start()
        thread_diskio.start()
        thread_network.start()
        thread_system.start()
        thread_version.start()
        thread_get.start()

        # Short execution framewor
        frames = Frames()
        time.sleep(1)
        term.clear()
        term.pos(1, 0)
        frames.header()
        term.pos(2, 0)
        time.sleep(3)

        # Judge the input and exit
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        tty.setraw(sys.stdin.fileno())
        quit = sys.stdin.read(1)
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        if len(quit) == 1:
            flag = False
            time.sleep(1)
            que.queue.clear()
            # Reduction of the cursor
            os.system("echo -e \033[?25h")
            term.pos(1, 0)
            term.clear()


class Manage(object):
    """Manage the operations of each class"""

    def __init__(self, name):
        self.name = name

    def mamage_put(self):
        """Threads are specified by reflection as methods"""

        frames = Frames()
        while flag:
            getattr(frames, self.name)()
            time.sleep(0.1)

    def mamage_get(self):
        """Output the value under the fixed method according to the category"""
        
        while flag:
            value = que.get()
            value_type = value["type"]
            if value_type == "cpu":
                self.mamage_cpu(value)
            if value_type == "memory":
                self.mamage_memory(value)
            if value_type == "swap":
                self.mamage_swap(value)
            if value_type == "disk":
                self.mamage_disk(value)
            if value_type == "diskio":
                self.mamage_diskio(value)
            if value_type == "network":
                self.mamage_network(value)
            if value_type == "system":
                self.mamage_system(value)
            if value_type == "version":
                self.mamage_version(value)
            if value_type == "process":
                self.mamage_process(value)
            # Second judgment to clean message queue
            if flag == False:
                que.queue.clear()
            time.sleep(0.01)

    def mamage_cpu(self, value):
        """CPU output format"""
        
        term.pos(7, 4)
        term.write("CPU", term.bold)
        term.pos(7, 19)
        term.write("     ")
        term.pos(7, 8)
        # Output progress bar
        percent = ("%s%%" % (int(value["total"])))
        term.write("[%-10s]%s" % ("|" * int(value["total"]/10), percent))
        term.pos(7, 30)
        term.write("-CPU-", term.bold)
        term.pos(7, 45)
        term.write("        ")
        term.pos(7, 39)
        term.write("total: %s %%" % (round(value["total"], 1)))
        term.pos(7, 60)
        term.write("        ")
        term.pos(7, 55)
        term.write("used: %s %%" % (round(value["user"], 1)))
        term.pos(7, 75)
        term.write("        ")
        term.pos(7, 70)
        term.write("syst: %s %%" % (round(value["system"], 1)))
        term.pos(8, 45)
        term.write("        ")
        term.pos(8, 39)
        term.write("iowai: %s %%" % (round(value["iowait"], 1)))
        term.pos(8, 60)
        term.write("        ")
        term.pos(8, 55)
        term.write("nice: %s %%" % (round(value["nice"], 1)))
        term.pos(8, 75)
        term.write("        ")
        term.pos(8, 70)
        term.write("nice: %s %%" % (round(value["idle"], 1)))
        term.pos(7, 4)

    def mamage_memory(self, value):
        """Memory output format"""
        
        term.pos(9, 4)
        term.write("Mem", term.bold)
        term.pos(9, 8)
        total = (value["used"]/value["total"]) * 100
        percent = ("%s%%" % (int(total)))
        term.write("[%-10s]%s" % ("|" * int(total/10), percent))
        term.pos(9, 30)
        term.write("-MEM-", term.bold)
        term.pos(9, 39)
        term.write("total: %s MB" % (int(value["total"])))
        term.pos(9, 55)
        term.write("used: %s MB" % (int(value["used"])))
        term.pos(9, 70)
        term.write("free: %s MB" % (int(value["free"])))
        term.pos(10, 39)
        term.write("activ: %s MB" % (int(value["active"])))
        term.pos(10, 55)
        term.write("buff: %s MB" % (int(value["buffers"])))
        term.pos(10, 70)
        term.write("cach: %s MB" % (int(value["cached"])))
        term.pos(9, 4)

    def mamage_swap(self, value):
        """Swap output format"""
        
        term.pos(11, 3)
        term.write("Swap", term.bold)
        term.pos(11, 8)
        # Determine if the value is 0 and the exception is caught
        try:
            total = (int(value["used"])/int(value["total"])) * 100
        except ZeroDivisionError:
            total = 0
        percent = ("%s%%" % (int(total)))
        term.write("[%-10s]%s" % ("|" * int(total/10), percent))
        term.pos(11, 30)
        term.write("-Swap-", term.bold)
        term.pos(11, 39)
        term.write("total: %s MB" % (int(value["total"])))
        term.pos(11, 55)
        term.write("used: %s MB" % (int(value["used"])))
        term.pos(11, 70)
        term.write("free: %s MB" % (int(value["free"])))
        term.pos(12, 41)
        term.write("sin: %s MB" % (int(value["sin"])))
        term.pos(12, 55)
        term.write("sout: %s MB" % (int(value["sout"])))
        term.pos(12, 70)
        term.write("perc: %s %%" % (str(value["percent"])))
        term.pos(11, 3)

    def mamage_disk(self, value):
        """Disk output format"""
        
        term.pos(13, 3)
        term.write("Disk", term.bold)
        term.pos(13, 8)
        total = (value["used"]/value["total"]) * 100
        percent = ("%s%%" % (int(total)))
        term.write("[%-10s]%s" % ("|" * int(total/10), percent))
        term.pos(13, 30)
        term.write("-Disk-", term.bold)
        term.pos(13, 39)
        term.write("total: %s GB" % (int(value["total"])))
        term.pos(13, 55)
        term.write("used: %s GB" % (int(value["used"])))
        term.pos(13, 70)
        term.write("free: %s GB" % (int(value["free"])))
        term.pos(13, 3)

    def mamage_system(self, value):
        """System output format"""
        
        day, now = time.strftime("%Y-%m-%d %H:%M:%S").split()
        course_pid = psutil.pids()
        course_count = 0
        for i in course_pid:
            course_count = course_count + 1

        term.pos(2, 4)
        term.write("USER: " + str(value["username"]))
        term.pos(2, 16)
        term.write("T: " + str(value["terminal"]))
        term.pos(2, 28)
        term.write("-")
        term.pos(2, 33)
        term.write("Process: " + str(course_count))
        term.pos(2, 48)
        term.write("-")
        term.pos(2, 53)
        term.write("BootTime: " + str(value["BootTime"]))
        term.pos(4, 4)
        term.write("HOST: " + str(value["hostname"]))
        term.pos(4, 28)
        term.write("-")
        term.pos(4, 32)
        term.write("Sec: " + str(now))
        term.pos(4, 48)
        term.write("-")
        term.pos(4, 53)
        term.write("LogiTime: " + str(value["started"]))
        term.pos(2, 3)

    def mamage_network(self, value):
        """Network output format"""
        
        term.pos(20, 68)
        term.clearLineFromPos()
        term.write("TX: " + str(round(value["send"], 2)) + " KB")
        term.pos(20, 88)
        term.write("|", term.bold)
        term.pos(21, 68)
        term.clearLineFromPos()
        term.write("RX: " + str(round(value["recv"], 2)) + " KB")
        term.pos(21, 88)
        term.write("|", term.bold)
        term.pos(22, 67)
        term.write("TXP: " + str(value["packets_sent"]))
        term.pos(23, 67)
        term.write("TXP: " + str(value["packets_recv"]))
        term.pos(20, 68)

    def mamage_diskio(self, value):
        """Disk IO output format"""
        
        term.pos(31, 68)
        term.clearLineFromPos()
        term.write("Read: " + str(round(value["read"], 2)) + " KB")
        term.pos(31, 88)
        term.write("|", term.bold)
        term.pos(32, 68)
        term.clearLineFromPos()
        term.write("Wrtn: " + str(round(value["write"], 2)) + " KB")
        term.pos(32, 88)
        term.write("|", term.bold)
        term.pos(33, 68)
        term.write("Rsec: " + str(value["read_count"]))
        term.pos(34, 68)
        term.write("Wsec: " + str(value["write_count"]))
        term.pos(35, 69)
        term.write("Tps: " + str(value["tps"]))
        term.pos(32, 68)

    def mamage_process(self, value):
        """Process output format"""
        
        value = value["key"]
        count = 19
        # Loop outputs each process
        for v in value:
            term.pos(count, 3)
            term.write(v["user"])
            term.pos(count, 11)
            term.write(str(v["pid"]))
            term.pos(count, 18)
            term.write(str(v["cpu"]))
            term.pos(count, 26)
            term.write(str(round(v["memory"], 2)))
            term.pos(count, 34)
            term.write(str(v["threads"]))
            term.pos(count, 42)
            term.write(str(v["name"]))
            count = count + 1
        term.pos(18, 4)

    def mamage_version(self, value):
        """Version of the output"""
        
        term.pos(16, 3)
        term.write(value["system"])
        term.pos(16, 10)
        term.write(value["version"])


class Frames(object):
    """Terminal screen module"""

    def header(self):
        """Frame structure format output"""

        # upper part
        bold = term.format("#", term.bold)
        frame_up = bold.ljust(100, "=")
        frame_up_format = term.format(frame_up)
        term.write(frame_up_format+bold)

        # center section 1
        term.pos(3, 0)
        frame_three = term.format("+".ljust(87, "-"))
        term.write(frame_three+"+")

        # center section 2
        term.pos(5, 0)
        frame_five = term.format("+".ljust(87, "-"))
        term.write(frame_five+"+")

        # center section 3
        frame_centre1 = "+".ljust(87, "=")
        term.pos(15, 0)
        term.write(frame_centre1+"+")

        # center section 4
        frame_centre2 = "+".ljust(59, "=")
        term.pos(17, 0)
        term.write(frame_centre2)
        term.pos(17, 88)
        term.write("|", term.bold)

        # Producer information
        kevin = "Kevin.Xiang"
        term.pos(16, 47)
        term.write(kevin)

        # next part
        frame_down = bold.ljust(100, "=")
        term.pos(39, 0)
        term.write(frame_down+bold)

        # border style
        for i1 in range(7, 14):
            term.pos(i1, 26)
            term.write("|")

        for i2 in range(16, 39):
            term.pos(i2, 60)
            term.write("|", term.bold)

        # Border output style IO
        term.pos(16, 61)
        frame_back = term.format("".rjust(27, " "), term.bgwhite)
        term.write(frame_back)
        term.pos(16, 71)
        frame_network = term.format("NETWORK", term.black, term.bgwhite)
        term.write(frame_network)
        term.pos(27, 61)
        term.write(frame_back)
        term.pos(27, 73)
        frame_disk = term.format("DISK", term.black, term.bgwhite)
        term.write(frame_disk)

        # Process output style
        term.pos(18, 0)
        space = "".center(4, " ")
        frame = term.format("  USER"
                            + space
                            + "PID"
                            + space
                            + "CPU%"
                            + space
                            + "MEM%"
                            + space
                            + "THRE"
                            + space
                            + "NAME", term.bold)
        term.write(frame)

        # Border output style
        list_down = [2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 19, 20, 21,
                     22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]
        for i3 in list_down:
            term.pos(i3, 0)
            term.write("|", term.bold)
            term.pos(i3, 88)
            term.write("|", term.bold)

    def frames_cpu(self):
        """CPU statistics"""
        
        t1 = psutil.cpu_times()
        time.sleep(1)
        t2 = psutil.cpu_times()

        value = []
        for v1, v2 in zip(t1, t2):
            value.append(v2-v1)

        count = 0
        for v in value:
            count = count + v

        user = value[0]
        nice = value[1]
        system = value[2]
        idle = value[3]
        iowait = value[4]
        irq = value[5]
        softirq = value[6]
        steal = value[7]
        guest = value[8]
        guest_nice = value[9]
        total = count

        cpu = Cpu(user, nice, system, idle, iowait,
                  irq, softirq, steal, guest, guest_nice, total)

        cpu_out = {
            "total": cpu.cpu_total(),
            "user": cpu.cpu_user(),
            "system": cpu.cpu_system(),
            "idle": cpu.cpu_idle(),
            "iowait": cpu.cpu_iowait(),
            "nice": cpu.cpu_nice(),
            "type": "cpu"
        }

        que.put(cpu_out)

    def frames_memory(self):
        """Memory statistics"""
        
        time.sleep(1)
        value = psutil.virtual_memory()
        used = value.used
        free = value.free
        active = value.active
        inactive = value.inactive
        buffers = value.buffers
        cached = value.cached
        total = value.total

        memory = Memory(used, free, active, inactive,
                        buffers, cached, total)

        memory_out = {
            "total": memory.memory_total(),
            "used": memory.memory_used(),
            "free": memory.memory_free(),
            "active": memory.memory_active(),
            "buffers": memory.memory_buffers(),
            "cached": memory.memory_cached(),
            "type": "memory"
        }
        que.put(memory_out)

    def frames_swap(self):
        """Swap information statistics"""
        
        time.sleep(1)
        value = psutil.swap_memory()
        used = value.used
        free = value.free
        sin = value.sin
        sout = value.sout
        total = value.total
        percent = value.percent

        swap = Swap(used, free, sin, sout, total, percent)

        swap_out = {
            "total": swap.swap_total(),
            "used": swap.swap_used(),
            "free": swap.swap_free(),
            "sin": swap.swap_sin(),
            "sout": swap.swap_sout(),
            "percent": swap.swap_percent(),
            "type": "swap"
        }

        que.put(swap_out)

    def frames_disk(self):
        """Information statistics only get / contents disk"""
        
        time.sleep(1)
        value = psutil.disk_usage('/')
        used = value.used
        free = value.free
        total = value.total

        disk = Disk(used, free, total)

        disk_out = {
            "total": disk.disk_total(),
            "used": disk.disk_used(),
            "free": disk.disk_free(),
            "type": "disk"
        }

        que.put(disk_out)

    def frames_diskio(self):
        """Disk IO statistics"""
        
        t1_diskio = psutil.disk_io_counters()
        time.sleep(1)
        t2_diskio = psutil.disk_io_counters()

        read = t2_diskio.read_bytes - t1_diskio.read_bytes
        write = t2_diskio.write_bytes - t1_diskio.write_bytes
        read_count = t2_diskio.read_count - t1_diskio.read_count
        write_count = t2_diskio.write_count - t1_diskio.write_count
        tps = t2_diskio.read_count + t2_diskio.write_count - \
            t1_diskio.read_count - t1_diskio.write_count

        diskio = Diskio(read, write, read_count, write_count, tps)

        diskio_out = {
            "read": diskio.diskio_read(),
            "write": diskio.diskio_write(),
            "read_count": diskio.diskio_read_count(),
            "write_count": diskio.diskio_write_count(),
            "tps": diskio.diskio_tps(),
            "type": "diskio"
        }
        que.put(diskio_out)

    def frames_network(self):
        """Network statistics"""
        
        t1 = psutil.net_io_counters()
        time.sleep(1)
        t2 = psutil.net_io_counters()

        value = []
        for v1, v2 in zip(t1, t2):
            value.append(v2-v1)

        bytes_sent = value[0]
        bytes_recv = value[1]
        packets_sent = value[2]
        packets_recv = value[3]

        network = Network(bytes_sent, bytes_recv,
                          packets_sent, packets_recv)

        network_out = {
            "send": network.network_bytes_sent(),
            "recv": network.network_bytes_recv(),
            "packets_sent": network.network_packets_sent(),
            "packets_recv": network.network_packets_recv(),
            "type": "network"
        }

        que.put(network_out)

    def frames_system(self):
        """System of statistical"""
        
        time.sleep(1)
        boot_time = psutil.boot_time()
        tty = os.popen("tty").read().replace('/dev/', '', 1).strip()
        value = psutil.users()
        for v in value:
            if v.terminal == tty:
                username = v.name
                terminal = v.terminal
                hostname = v.host
                started = v.started
                userpid = v.pid

        system = System(boot_time, username,
                        terminal, hostname, started, userpid)

        system_out = {
            "BootTime": system.system_boot_time(),
            "username": system.system_username(),
            "terminal": system.system_terminal(),
            "hostname": system.system_hostname(),
            "started": system.system_started(),
            "userpid": system.system_userpid(),
            "type": "system",
        }
        que.put(system_out)

    def frames_version(self):
        """Version statistics"""
        
        time.sleep(1)
        value = platform.uname()
        system = value.system
        localhost = value.node
        kernel = value.release
        sysver = value.version
        machine = value.machine

        version = Version(system, localhost, kernel, sysver, machine)

        version_out = {
            "system": version.version_system(),
            "localhost": version.version_localhost(),
            "kernel": version.version_kernel(),
            "version": version.version_sysver(),
            "machine": version.version_machine(),
            "type": "version"
        }

        que.put(version_out)

    def frames_process(self):
        """Process statistics"""
        
        time.sleep(1)
        list1 = []

        PID = psutil.pids()

        for p in PID:
            try:
                proc = psutil.Process(p)
                user = proc.uids()[0]
                name = proc.name()
                pid = p
                cpu = proc.cpu_percent(interval=0)
                memory = proc.memory_percent()
                status = proc.status()
                threads = proc.num_threads()

                process = Process(user, name, pid, cpu,
                                  memory, status, threads)
                dist1 = {
                    "user": process.process_user(),
                    "name": process.process_name(),
                    "pid": process.process_pid(),
                    "cpu": process.process_cpu(),
                    "memory": process.process_memory(),
                    "status": process.process_status(),
                    "threads": process.process_threads(),
                }
                list1.append(dist1)
            except:
                continue

        # Arrange by key in the dictionary
        list2 = sorted(list1, key=lambda x: x["threads"], reverse=True)

        list3 = []
        count = 0
        for p2 in list2:
            list3.append(p2)
            count = count + 1
            if count == 19:
                break

        process_out = {
            "key": list3,
            "type": "process"
        }

        que.put(process_out)


class Cpu(object):
    """ CPU usage information """

    def __init__(self, user, nice, system, idle, iowait, irq,
                 softirq, steal, guest, guest_nice, total):

        self.user = user
        self.nice = nice
        self.system = system
        self.idle = idle
        self.iowait = iowait
        self.irq = irq
        self.softirq = softirq
        self.steal = steal
        self.guest = guest
        self.guest_nice = guest_nice
        self.total = total

    def cpu_user(self):
        """User utilization"""

        cpu_user = (self.user / self.total) * 100
        return cpu_user

    def cpu_nice(self):
        """Nice usage rate"""

        cpu_nice = (self.nice / self.total) * 100
        return cpu_nice

    def cpu_system(self):
        """System utilization"""

        cpu_system = (self.system / self.total) * 100
        return cpu_system

    def cpu_idle(self):
        """CPU available space"""

        cpu_idle = (self.idle / self.total) * 100
        return cpu_idle

    def cpu_iowait(self):
        """Disk IO usage"""

        cpu_iowait = (self.iowait / self.total) * 100
        return cpu_iowait

    def cpu_total(self):
        """The total usage"""

        cpu_total = self.user
        cpu_total = ((self.total - self.idle) / self.total) * 100
        return cpu_total


class Memory(object):
    """Memory information details"""

    def __init__(self, used, free, active, inactive, buffers, cached, total):

        self.used = used
        self.free = free
        self.active = active
        self.inactive = inactive
        self.buffers = buffers
        self.cached = cached
        self.total = total

    def memory_used(self):
        """Memory user usage"""

        memory_used = self.used/1024/1024
        return memory_used

    def memory_free(self):
        """The true remaining memory size"""

        memory_free = self.free/1024/1024
        return memory_free

    def memory_active(self):
        """The memory program considers the size available to contain the cache buffer"""

        memory_active = self.active/1024/1024
        return memory_active

    def memory_inactive(self):
        """Unused memory does not contain caches"""

        memory_inactive = self.inactive/1024/1024
        return memory_inactive

    def memory_buffers(self):
        """Buffer usage memory"""

        memory_buffers = self.buffers/1024/1024
        return memory_buffers

    def memory_cached(self):
        """Unused memory does not contain caches"""

        memory_cached = self.cached/1024/1024
        return memory_cached

    def memory_total(self):
        """Total memory size"""

        memory_total = self.total/1024/1024
        return memory_total


class Swap(object):
    """Virtual memory information"""

    def __init__(self, used, free, sin, sout, total, percent):
        self.used = used
        self.free = free
        self.sin = sin
        self.sout = sout
        self.total = total
        self.percent = percent

    def swap_used(self):
        """Virtual memory used by users"""

        swap_used = self.used/1024/1024
        return swap_used

    def swap_free(self):
        """Virtual memory remaining space"""

        swap_free = self.free/1024/1024
        return swap_free

    def swap_sin(self):
        """The system accumulates the number of MB swapped in from disk"""

        swap_sin = self.sin/1024/1024
        return swap_sin

    def swap_sout(self):
        """The number of MB the system accumulates from disk """

        swap_sout = self.sin/1024/1024
        return swap_sout

    def swap_total(self):
        """Total virtual memory size"""

        swap_total = self.total/1024/1024
        return swap_total

    def swap_percent(self):
        """Using percentage swap"""

        swap_percent = self.percent
        return swap_percent


class Disk(object):
    """Disk resource information"""

    def __init__(self, used, free, total):
        self.used = used
        self.free = free
        self.total = total

    def disk_used(self):
        """Disk user use GB """

        disk_used = self.used/1024/1024/1024
        return disk_used

    def disk_free(self):
        """Disk space GB"""

        disk_free = self.free/1024/1024/1024
        return disk_free

    def disk_total(self):
        """Total disk size GB"""

        disk_total = self.total/1024/1024/1024
        return disk_total


class Diskio(object):
    """View disk IO"""

    def __init__(self, read, write, read_count, write_count, tps):
        self.read = read
        self.write = write
        self.read_count = read_count
        self.write_count = write_count
        self.tps = tps

    def diskio_read(self):
        """A disk read kb"""

        diskio_read = self.read/1024
        return diskio_read

    def diskio_write(self):
        """A disk read kb"""

        diskio_write = self.write/1024
        return diskio_write

    def diskio_read_count(self):
        """Merge reads"""

        diskio_read_count = self.read_count
        return diskio_read_count

    def diskio_write_count(self):
        """Merge write times"""

        diskio_write_count = self.write_count
        return diskio_write_count

    def diskio_tps(self):
        """Read/write IO handles a response transaction"""

        diskio_tps = self.tps
        return diskio_tps


class Network(object):
    """Network resource information"""

    def __init__(self, bytes_sent, bytes_recv, packets_sent, packets_recv):
        self.bytes_sent = bytes_sent
        self.bytes_recv = bytes_recv
        self.packets_sent = packets_sent
        self.packets_recv = packets_recv

    def network_bytes_sent(self):
        """The network sends packets in kilobytes per second"""

        network_bytes_sent = self.bytes_sent/1024
        return network_bytes_sent

    def network_bytes_recv(self):
        """The network receives traffic in kilobytes per second"""

        network_bytes_recv = self.bytes_recv/1024
        return network_bytes_recv

    def network_packets_sent(self):
        """Number of packets sent per second"""

        network_packets_sent = self.packets_sent
        return network_packets_sent

    def network_packets_recv(self):
        """Number of packets received per second"""

        network_packets_recv = self.packets_recv
        return network_packets_recv


class System(object):
    """System resource information"""

    def __init__(self, boot_time, username, terminal, hostname, started, userpid):
        self.boot_time = boot_time
        self.username = username
        self.terminal = terminal
        self.hostname = hostname
        self.started = started
        self.userpid = userpid

    def system_boot_time(self):
        """System startup time"""

        system_boot_time = datetime.datetime.fromtimestamp(
            self.boot_time).strftime("%Y-%m-%d %H:%M:%S")
        return system_boot_time

    def system_username(self):
        """Current logged-in user"""

        system_username = self.username
        return system_username

    def system_terminal(self):
        """User access terminal"""

        system_terminal = self.terminal
        return system_terminal

    def system_hostname(self):
        """Connect user IP"""

        system_hostname = self.hostname
        return system_hostname

    def system_started(self):
        """User time"""

        system_started = datetime.datetime.fromtimestamp(
            self.started).strftime("%Y-%m-%d %H:%M:%S")

        return system_started

    def system_userpid(self):
        """User pid"""

        system_userpid = self.userpid
        return system_userpid


class Version(object):
    """system version"""

    def __init__(self, system, localhost, kernel, sysver, machine):
        self.system = system
        self.localhost = localhost
        self.kernel = kernel
        self.sysver = sysver
        self.machine = machine

    def version_system(self):
        """system type"""

        version_system = self.system
        return version_system

    def version_localhost(self):
        """Localhost name"""

        version_localhost = self.localhost
        return version_localhost

    def version_kernel(self):
        """Kernel version"""

        version_kernel = self.kernel
        return version_kernel

    def version_sysver(self):
        """system version"""

        version_sysver = self.sysver
        return version_sysver

    def version_machine(self):
        """System digits"""

        version_machine = self.machine
        return version_machine


class Process(object):
    """Process information"""

    def __init__(self, user, name, pid, cpu, memory, status, threads):
        self.user = user
        self.name = name
        self.pid = pid
        self.cpu = cpu
        self.memory = memory
        self.status = status
        self.threads = threads

    def process_user(self):
        process_user = os.popen(
            "getent passwd %s | awk -F':' '{print $1}'" % (self.user))
        user = process_user.read()
        process_user = user

        return process_user

    def process_name(self):
        """process name"""

        process_name = self.name
        return process_name

    def process_pid(self):
        """process pid"""

        process_pid = self.pid
        return process_pid

    def process_cpu(self):
        """process cpu"""

        process_cpu = self.cpu

        return process_cpu

    def process_memory(self):
        """process memory"""

        process_memory = self.memory
        return process_memory

    def process_status(self):
        """process status"""

        process_status = self.status
        return process_status

    def process_threads(self):
        """process threads"""

        process_threads = self.threads
        return process_threads


if __name__ == '__main__':
    que = queue.Queue()
    start = Run()
    os.system("echo -e \033[?25l")
    start.run()
