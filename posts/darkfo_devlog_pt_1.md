This is the first part in what may or may not become a series, but it is a post on a project I have been working on for a few weeks -- a project that aims to help me learn about the internals of the [*Fallout 2*](http://en.wikipedia.org/wiki/Fallout_2) engine and recreate parts of it along the way.

This would ideally take place in the beginning of my journey through the Wasteland, but I didn't think I would make it this far and so I did not consider starting such a development blog.

Without further adieu, thus start part one, my journey into ScriptTown.

Fallout Scripting
-----------------

[*Fallout 2*](http://en.wikipedia.org/wiki/Fallout_2) is scripted with a proprietary dialect of [Pascal](http://en.wikipedia.org/wiki/Pascal_(programming_language)). It's a basic imperative and procedural language, with your usual structural constructs (`if`, `while`), variables, etc. It's extended through the usage of the C preprocessor. Originally, the developers used (and today, modders still use) the Watcom C compiler's preprocessor. However, any C preprocessor works -- I use `cpp(1)` from gcc (provided by MinGW).

The game's original (sparsely commented) scripts are provided by the official *Mapper* tool later released by the developers.

The scripts are compiled (with a proprietary, 16-bit DOS compiler) from `.SSL` files to a proprietary bytecode `.INT` files, which the engine then loads and runs.

 Here's an example of a game script (property of Interplay):

    #include "..\headers\define.h"
    #include "..\headers\ArBridge.h"
    #include "..\headers\updatmap.h"
    
    #define NAME SCRIPT_ARBRIDGE
    
    #include "..\headers\command.h"
    
    procedure start;
    procedure map_enter_p_proc;
    procedure map_update_p_proc;
    
    procedure start begin
    end
    
    procedure map_enter_p_proc begin
       if (map_first_run) then begin
           display_msg(mstr(100));
           mark_klamath_on_map
       end
    
       if ((map_var(MVAR_Made_Car) == 0) and (global_var(GVAR_PLAYER_GOT_CAR) != 0) and (car_current_town == AREA_ARROYO))     then begin
           set_map_var(MVAR_Made_Car,1);
           Create_Car(CAR_ARROYO_HEX,CAR_ARROYO_ELEV)
       end
    
       else if ((map_var(MVAR_Made_Car) == 1) and (car_current_town != AREA_ARROYO)) then begin
           set_map_var(MVAR_Made_Car,0);
           Dest_Car(CAR_ARROYO_HEX,CAR_ARROYO_ELEV)
       end
    
       Lighting;
    
       set_global_var(GVAR_LOAD_MAP_INDEX,0);
    
    end
    
    procedure map_update_p_proc begin
       Lighting;
    end

The `#include`s substitute in some common code. `NAME` is used by some of the macros there (like `mstr` which is a partially evaluated `message_str` using the map ID).

`map_enter_p_proc` is called whenever the map is entered into, and `map_update_p_proc` is called occasionally.

`map_var` and `set_map_var` are used to access *MVAR*s -- persistent map-local variables. *LVAR*s are persistent script-local variables, and *GVAR*s are persistent global variables.

So, we can guess what the program does upon map entry:

  - If this is our first time entering this map, display map message with ID 100, and mark the city *Klamath* on our map. (This is one of the beginning maps, *Klamath* being the next city you'll visit. `mark_klamath_on_map` is a macro, as you might can guess.)
  - If we have a car, and our car is in this area (*Arroyo*), then set the car here and spawn it.
  - Set up map lighting (this is a macro, too. A particularly ugly one, as you'll see later.)
  - Set the global variable "load map index" to 0.

and upon update:

  - Update lighting

The latter is done because in-game time progresses and there is a day/night cycle, complete with varying lighting levels.

This script expands (after preprocessing) to the following:

    variable ProtoOfItemGiven;
    variable ValueOfRollCheck:=1;
    variable Scenery_Creation;
    variable Scenery_Creation_Hex;
    variable Scenery_Creation_Count;
    variable Temp_Scenery_Creation_Hex;
    variable Scenery_Creation_Ptr;
    
    variable How_Many_Party_Members_Are_Injured;
    variable How_Many_Party_Members_Armed;
    variable PartyHealingItem;
    procedure checkPartyMembersNearDoor begin
       if ((party_member_obj((16777278)) != 0)) then begin if (tile_distance_objs(self_obj, party_member_obj((16777278))) <    = (5)) then begin return 1; end end
       if ((party_member_obj((16777376)) != 0)) then begin if (tile_distance_objs(self_obj, party_member_obj((16777376))) <    = (5)) then begin return 1; end end
       if ((party_member_obj((16777377)) != 0)) then begin if (tile_distance_objs(self_obj, party_member_obj((16777377))) <    = (5)) then begin return 1; end end
       if ((party_member_obj((16777305)) != 0)) then begin if (tile_distance_objs(self_obj, party_member_obj((16777305))) <    = (5)) then begin return 1; end end
       if ((party_member_obj((16777313)) != 0)) then begin if (tile_distance_objs(self_obj, party_member_obj((16777313))) <    = (5)) then begin return 1; end end
       if ((party_member_obj((16777323)) != 0)) then begin if (tile_distance_objs(self_obj, party_member_obj((16777323))) <    = (5)) then begin return 1; end end
       if ((party_member_obj((16777352)) != 0)) then begin if (tile_distance_objs(self_obj, party_member_obj((16777352))) <    = (5)) then begin return 1; end end
       if ((party_member_obj((16777378)) != 0)) then begin if (tile_distance_objs(self_obj, party_member_obj((16777378))) <    = (5)) then begin return 1; end end
       if ((party_member_obj((16777368)) != 0)) then begin if (tile_distance_objs(self_obj, party_member_obj((16777368))) <    = (5)) then begin return 1; end end
       if ((party_member_obj((16777379)) != 0)) then begin if (tile_distance_objs(self_obj, party_member_obj((16777379))) <    = (5)) then begin return 1; end end
       if ((party_member_obj((16777380)) != 0)) then begin if (tile_distance_objs(self_obj, party_member_obj((16777380))) <    = (5)) then begin return 1; end end
       if ((party_member_obj((16777295)) != 0)) then begin if (tile_distance_objs(self_obj, party_member_obj((16777295))) <    = (5)) then begin return 1; end end
       if ((party_member_obj((16777381)) != 0)) then begin if (tile_distance_objs(self_obj, party_member_obj((16777381))) <    = (5)) then begin return 1; end end
       if ((party_member_obj((16777407)) != 0)) then begin if (tile_distance_objs(self_obj, party_member_obj((16777407))) <    = (5)) then begin return 1; end end
       if ((party_member_obj((16777411)) != 0)) then begin if (tile_distance_objs(self_obj, party_member_obj((16777411))) <    = (5)) then begin return 1; end end
       if ((party_member_obj((16777412)) != 0)) then begin if (tile_distance_objs(self_obj, party_member_obj((16777412))) <    = (5)) then begin return 1; end end
       if ((party_member_obj((16777413)) != 0)) then begin if (tile_distance_objs(self_obj, party_member_obj((16777413))) <    = (5)) then begin return 1; end end
       if ((party_member_obj((16777481)) != 0)) then begin if (tile_distance_objs(self_obj, party_member_obj((16777481))) <    = (5)) then begin return 1; end end
       if ((party_member_obj((16777558)) != 0)) then begin if (tile_distance_objs(self_obj, party_member_obj((16777558))) <    = (5)) then begin return 1; end end
       if ((party_member_obj((16777600)) != 0)) then begin if (tile_distance_objs(self_obj, party_member_obj((16777600))) <    = (5)) then begin return 1; end end
       return 0;
    end
    variable global_temp;
    variable dest_tile;
    variable step_tile;
    variable in_dialog;
    variable forced_node;
    variable restock_amt;
    variable restock_obj;
    variable restock_trash;
    variable removed_qty;
    procedure start;
    procedure map_enter_p_proc;
    procedure map_update_p_proc;
    procedure start begin
    end
    procedure map_enter_p_proc begin
       if (metarule(14, 0)) then begin
           display_msg(message_str((28),100));
           if (metarule(17, (2)) == (0)) then begin debug_msg("  mark_on_map("+(2)+")"); mark_area_known((0), (2), (1)); end
       end
       if ((map_var((0)) == 0) and (global_var((18)) != 0) and (metarule(30, 0) == (0))) then begin
           set_map_var((0),1);
           if ((not(metarule(22, 0))) and ((global_var((18)) != 0) or (cur_map_index == (6)))) then begin     Scenery_Creation:=create_object_sid((33555441),(27312),(0), (304)); Scenery_Creation_Hex:=(27312);     Scenery_Creation_Count:=0; while (Scenery_Creation_Count < 2) do begin     Scenery_Creation_Hex:=tile_num_in_direction(Scenery_Creation_Hex,1,1); Scenery_Creation:=create_object_sid((    33554499),Scenery_Creation_Hex,(0),-1); Scenery_Creation_Count+=1; end Scenery_Creation_Count:=0; while (    Scenery_Creation_Count < 2) do begin Scenery_Creation_Hex:=tile_num_in_direction(Scenery_Creation_Hex,2,1);     Scenery_Creation:=create_object_sid((33554499),Scenery_Creation_Hex,(0),-1); Scenery_Creation_Count+=1; end     Scenery_Creation_Count:=0; while (Scenery_Creation_Count < 2) do begin     Scenery_Creation_Hex:=tile_num_in_direction(Scenery_Creation_Hex,3,1); Scenery_Creation:=create_object_sid((    33554499),Scenery_Creation_Hex,(0),-1); Scenery_Creation_Count+=1; end Scenery_Creation_Count:=0; while (    Scenery_Creation_Count < 2) do begin Scenery_Creation_Hex:=tile_num_in_direction(Scenery_Creation_Hex,4,1);     Scenery_Creation:=create_object_sid((33554499),Scenery_Creation_Hex,(0),-1); Scenery_Creation_Count+=1; end     Scenery_Creation_Count:=0; while (Scenery_Creation_Count < 1) do begin     Scenery_Creation_Hex:=tile_num_in_direction(Scenery_Creation_Hex,5,1); Scenery_Creation:=create_object_sid((    33554499),Scenery_Creation_Hex,(0),-1); Scenery_Creation_Count+=1; end Scenery_Creation_Count:=0; while (    Scenery_Creation_Count < 1) do begin Scenery_Creation_Hex:=tile_num_in_direction(Scenery_Creation_Hex,4,1);     Scenery_Creation:=create_object_sid((33554499),Scenery_Creation_Hex,(0),-1); Scenery_Creation_Count+=1; end     Scenery_Creation_Count:=0; while (Scenery_Creation_Count < 1) do begin     Scenery_Creation_Hex:=tile_num_in_direction(Scenery_Creation_Hex,5,1); Scenery_Creation:=create_object_sid((    33554499),Scenery_Creation_Hex,(0),-1); Scenery_Creation_Count+=1; end Scenery_Creation_Count:=0; while (    Scenery_Creation_Count < 1) do begin Scenery_Creation_Hex:=tile_num_in_direction(Scenery_Creation_Hex,4,1);     Scenery_Creation:=create_object_sid((33554499),Scenery_Creation_Hex,(0),-1); Scenery_Creation_Count+=1; end     Scenery_Creation_Count:=0; while (Scenery_Creation_Count < 1) do begin     Scenery_Creation_Hex:=tile_num_in_direction(Scenery_Creation_Hex,5,1); Scenery_Creation:=create_object_sid((    33554499),Scenery_Creation_Hex,(0),-1); Scenery_Creation_Count+=1; end Scenery_Creation_Count:=0; while (    Scenery_Creation_Count < 1) do begin Scenery_Creation_Hex:=tile_num_in_direction(Scenery_Creation_Hex,4,1);     Scenery_Creation:=create_object_sid((33554499),Scenery_Creation_Hex,(0),-1); Scenery_Creation_Count+=1; end     Scenery_Creation_Count:=0; while (Scenery_Creation_Count < 1) do begin     Scenery_Creation_Hex:=tile_num_in_direction(Scenery_Creation_Hex,0,1); Scenery_Creation:=create_object_sid((    33554499),Scenery_Creation_Hex,(0),-1); Scenery_Creation_Count+=1; end Scenery_Creation_Count:=0; while (    Scenery_Creation_Count < 1) do begin Scenery_Creation_Hex:=tile_num_in_direction(Scenery_Creation_Hex,5,1);     Scenery_Creation:=create_object_sid((33554499),Scenery_Creation_Hex,(0),-1); Scenery_Creation_Count+=1; end     Scenery_Creation_Count:=0; while (Scenery_Creation_Count < 2) do begin     Scenery_Creation_Hex:=tile_num_in_direction(Scenery_Creation_Hex,0,1); Scenery_Creation:=create_object_sid((    33554499),Scenery_Creation_Hex,(0),-1); Scenery_Creation_Count+=1; end Scenery_Creation_Count:=0; while (    Scenery_Creation_Count < 1) do begin Scenery_Creation_Hex:=tile_num_in_direction(Scenery_Creation_Hex,1,1);     Scenery_Creation:=create_object_sid((33554499),Scenery_Creation_Hex,(0),-1); Scenery_Creation_Count+=1; end     Scenery_Creation_Count:=0; while (Scenery_Creation_Count < 1) do begin     Scenery_Creation_Hex:=tile_num_in_direction(Scenery_Creation_Hex,2,1); Scenery_Creation:=create_object_sid((    33554499),Scenery_Creation_Hex,(0),-1); Scenery_Creation_Count+=1; end if (party_member_obj((455)) != 0) then     begin move_to(party_member_obj((455)),Scenery_Creation_Hex,(0)); debug_msg("Moving the Car Trunk"); end else     begin create_object_sid((455),Scenery_Creation_Hex,(0),(920)); debug_msg("Making new Trunk."); end     Scenery_Creation_Count:=0; while (Scenery_Creation_Count < 1) do begin     Scenery_Creation_Hex:=tile_num_in_direction(Scenery_Creation_Hex,1,1); Scenery_Creation:=create_object_sid((    33554499),Scenery_Creation_Hex,(0),-1); Scenery_Creation_Count+=1; end Scenery_Creation_Count:=0; while (    Scenery_Creation_Count < 1) do begin Scenery_Creation_Hex:=tile_num_in_direction(Scenery_Creation_Hex,2,1);     Scenery_Creation:=create_object_sid((33554499),Scenery_Creation_Hex,(0),-1); Scenery_Creation_Count+=1; end end
       end
       else if ((map_var((0)) == 1) and (metarule(30, 0) != (0))) then begin
           // omitted
       end
       if ((get_month >= 3) and (get_month < 5)) then if (((game_time_hour >= ((600))) and (game_time_hour < ((600) + 100)))    ) then set_light_level((game_time_hour - (600)) + (40)); else if (((game_time_hour >= ((600) + 100)) and (    game_time_hour < (1800)))) then set_light_level(100); else if (((game_time_hour >= ((1800))) and (game_time_hour < ((    1800) + 100)))) then set_light_level((100) - (game_time_hour - (1800))); else set_light_level((40)); else if ((    get_month >= 5) and (get_month < 9)) then if (((game_time_hour >= ((500))) and (game_time_hour < ((500) + 100))))     then set_light_level((game_time_hour - (500)) + (40)); else if (((game_time_hour >= ((500) + 100)) and (    game_time_hour < (1900)))) then set_light_level(100); else if (((game_time_hour >= ((1900))) and (game_time_hour < ((    1900) + 100)))) then set_light_level((100) - (game_time_hour - (1900))); else set_light_level((40)); else if ((    get_month >= 9) and (get_month < 11)) then if (((game_time_hour >= ((600))) and (game_time_hour < ((600) + 100))))     then set_light_level((game_time_hour - (600)) + (40)); else if (((game_time_hour >= ((600) + 100)) and (    game_time_hour < (1800)))) then set_light_level(100); else if (((game_time_hour >= ((1800))) and (game_time_hour < ((    1800) + 100)))) then set_light_level((100) - (game_time_hour - (1800))); else set_light_level((40)); else if (((    game_time_hour >= ((700))) and (game_time_hour < ((700) + 100)))) then set_light_level((game_time_hour - (700)) + (40    )); else if (((game_time_hour >= ((700) + 100)) and (game_time_hour < (1700)))) then set_light_level(100); else if ((    (game_time_hour >= ((1700))) and (game_time_hour < ((1700) + 100)))) then set_light_level((100) - (game_time_hour - (    1700))); else set_light_level((40));
       set_global_var((27),0);
    end
    procedure map_update_p_proc begin
       // omitted
    end


Not particularly pretty. The `Lighting` macro expands to a long chain of branching logic depending on the current in-game time, then performs globally mutable state changes. I'm sure it's a right pain to debug.

You'll notice that we've now gotten rid of our pretty macro constants, instead being replaced with magic numbers. This is, unfortunately, what the engine deals with (and, unfortunately, Lua was in its infancy when this game and its predecessor was developed.)

The Approach
------------

By this point in the project, I already have a map viewer and a map editor, with varying levels of completion. (The viewer is mostly all in-tact, the editor can view, place, and rotate relevant objects. It cannot export maps to *Fallout 2* format, yet.)

The next step (short of figuring out how the horrid animation system works) is to start work on the scripting engine. Now, I am writing the engine mostly in vanilla JavaScript (for a few reasons -- (a) I want it to run in-browser, (b) I didn't want to use *TypeScript* at first, because it slows me down reading its gigantic specification for its lack of documentation, and (c) I am a masochist.) The backend binary map parser is written in *Python* and exports to JSON and uses *GraphicsMagick* to help convert images to PNGs with alpha channels, and for relevant images, also atlases them.

I wanted scripts to be just plain JavaScript files -- I could `eval` them and interact with them like native objects. I could then implement a better library on top of this for new (non-interoperable) scripts.

First, in my sleepy haze, I attempted to use a series of regular expressions to replace parts of the preprocessed scripts to JavaScript. That worked fine, but then I ran into the problem that I could not access and introspect variables within it. I wanted to encapsulate scripts in a JavaScript object. And so, the next day (today!), I set off to do that.

I poured another language into the mix -- my favored Haskell. I used [*Peggy*](http://tanakh.github.io/Peggy) (a PEG parser) and quickly wrote a grammar to parse the Pascal dialect. After that was finished, I had a nice little AST I could do whatever I wanted with. I also quickly (~15 minutes!) wrote the [*transpiler*](http://en.wikipedia.org/wiki/Source-to-source_compiler) pass -- taking the AST and outputting strings of JavaScript.

I wrote a test HTML page with some JavaScript to load the resulting script file, then evaluate it using `new Function(body)`, then constructing it as an object, with its prototype set to my new `Script` object.

*It worked!*

The purpose of the `Script` object is to implement the library to interface with the game engine. It provides procedures such as `map_var`, `set_global_var`, etc. which are looked up through the prototype chain. I stubbed out a fair bit of used procedures in scripts. It works well.

Now I have a native object I can inspect and prod, calling procedures like `map_enter_p_proc` and seeing how they work. You can see what functions are stubbed that it uses, which you can then fill in with game logic. Some scripts contain debug messages which can help guide me with that. There is a `COMMANDS.DOC` graciously provided by *Mapper* which has a list of scripting procedures.

Conclusion
----------

Go with whatever solution to a problem that you're comfortable with. It would have taken me a lot longer if I had tried to abuse regex (to do even worse than parse HTML!), or to (re)write a program to dump bytecode into a readable representation, and then figure out what each opcode does, and how the bytecode interpreter works. (There have been reverse engineering attempts by the venerable and trusty *TeamX*; but unfortunately most of their documentation is in Russian.)



And remember: Hacking. Hacking never changes.