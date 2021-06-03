# Steps of Creating An `mcpi` Project
1. Start a server using whatever you like to use. Here're a few examples:
    * Bukkit ([Tutorial Here](https://thebreakdown.xyz/start-bukkit-server-minecraft/))
    * 开服侠 ([Website](http://www.kaifuxia.com))
2. Place the [RaspberryJuice JAR](https://dev.bukkit.org/projects/raspberryjuice) into the `plugin` directory.  
(If there's none, either create one or wait for the tool you use to create one when generating the world).
3. Run the server. 
4. If this sis done correctly, you should be able to connect to Minecraft with `mcpi`. Try joining the server
 at `localhost` *then* running the following code:
5. If you see the line 'Hello Minecraft' in the chat, congratulations! You can now use `mcpi` normally.

# References and Notes
**Bukkit** is a tool used for creating servers (local or public). It's like 开服侠 but more low-leveled (you need to
create and run `.bat` yourself).  
* You can download server JARs of other versions from [CraftBukkit](https://getbukkit.org/download/craftbukkit). They are
(hopefully) compatible with any server tool you use.  
* **Note:** You'll need to edit `eula.txt` in order to run the server.

**mcpi** is the library you use in Python to communicate with (RaspberryJuice modded) Minecraft.  
An API documentation can be found [here](https://www.stuffaboutcode.com/p/minecraft-api-reference.html).

**RaspberryJuice** is the mod (aka plugin) your Minecraft server must have to communicate with Python.
 