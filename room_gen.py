# import Room from django proj
#
# import RoomGenerator
#
# rg.grid

from random import randint

class Room:
    def __init__(self, id):
        self.id = id
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.is_accessible = True
        self.title = None
        self.description = "A room, "



def create_rooms(width=10, height=10):
    """
    [1, 2, 3, 4, 5,
     6, 7, 8, 9, 10,
     11,12,13,14,15,
     16,17,18,19,20,
     21,22,23,24,25,]
    """
    # create blank rooms
    rooms = [Room(id) for id in range(1, (width * height + 1))]

    # make some rooms inaccessible
    for _ in range(0, height*width//10):
        rand_num = randint(0, height*width-1)
        while rooms[rand_num].is_accessible == False:
            rand_num = randint(0, height*width-1)
        rooms[rand_num].is_accessible = False

    # set each room's directions
    for i in range(len(rooms)):
        room = rooms[i]
        room.title = f"Room {id}"
        room.description += f"{id}"
        n_index = i - width
        s_index = i + width
        e_index = i + 1
        w_index = i - 1

        if not rooms[i].is_accessible:
            continue

        if n_index >= 0:
            if rooms[n_index].is_accessible:
                room.n_to = n_index + 1
        if s_index < height * width:
            if rooms[s_index].is_accessible:
                room.s_to = s_index +1
        if e_index % width != 0 and e_index < len(rooms):
            if rooms[e_index].is_accessible:
                room.e_to = e_index + 1
        if i % width != 0:
            if rooms[w_index].is_accessible:
                room.w_to = w_index + 1

    # put rooms into rows
    rooms_in_rows = []

    start_index = 0
    for _ in range(height):
        row = rooms[start_index:start_index+width]
        start_index += width
        rooms_in_rows.append(row)

    return rooms
    # for room in rooms:
    #     print(room.id, room.is_accessible, room.n_to, room.s_to, room.e_to, room.w_to)
    # for row in rooms_in_rows:
    #     print(len(row))

rooms = create_rooms(15, 15)

    # rooms = [Room(id) for id in range(1,(width*height+1))]
    # id = 1
    # room = rooms[id-1]
    # min_doors = 2
    # last_direction = 'e'
    #
    # for room in rooms:
    #     # check if doors to north and east
    #     if id - width > 0:
    #         if rooms[id-width-1].s_to is not None:
    #             room.n_to = id-width
    #             min_doors -= 1
    #     if id > 2:
    #         if rooms[id-1-1].e_to is not None:
    #             room.w_to = id-1
    #             min_doors -= 1
    #
    #     # removed n and w because those are set by the room created already
    #     possible_room_directions = ['s', 'e']
    #
    #     # remove possibility to move into a wall
    #     if room.id > (width * height) - (width):
    #         possible_room_directions.remove('s')
    #     if room.id % width == 0:
    #         possible_room_directions.remove('e')
    #
    #     # check top, right room (this can probably be refined, but for now, we're saying you can
    #     # always go both directions from the corners)
    #     if id == width:
    #         room.s_to = id + width
    #     if id == width -1:
    #         room.e_to = width
    #     # check top right room
    #     if id == 1:
    #         room .e_to = 2
    #         room.s_to = 1 + width
    #     # check bottom, left room
    #     if id == width*height-width-1:
    #         room.e_to = id + 1
    #     if id == width*height - (2*width-1):
    #         room.s_to = id + width
    #     # check bottom, right room
    #     if id == width*height-1:
    #         room.e_to = id + 1
    #     if id == width*height:
    #         return rooms
    #
    #     if len(possible_room_directions) == 0:
    #         id += 1
    #     elif len(possible_room_directions) == 1:
    #         if possible_room_directions[0] == 'e':
    #             room.e_to = id + 1
    #         else:
    #             room.s_to = id + width
    #     else:
    #         number_of_doors = randint(min_doors, len(possible_room_directions))
    #         if number_of_doors == 2:
    #             room.s_to = id + width
    #             room.e_to = id + 1
    #         elif number_of_doors == 1:
    #             if last_direction == 'e':
    #                 last_direction = 's'
    #                 room.e_to = id + 1
    #             else:
    #                 last_direction = 'e'
    #                 room.s_to = id + width
    #     id += 1



# width = 5
# height = 5
# map = create_rooms(width, height)
# for room in map:
#     print(room.id, ":", room.n_to, room.s_to, room.e_to, room.w_to)



# def print_rooms(self):
#     '''
#     Print the rooms in room_grid in ascii characters.
#     '''
#
#     # Add top border
#     str = "# " * ((3 + width * 5) // 2) + "\n"
#
#     # The console prints top to bottom but our array is arranged
#     # bottom to top.
#     #
#     # We reverse it so it draws in the right direction.
#     reverse_grid = list(self.grid) # make a copy of the list
#     reverse_grid.reverse()
#     for row in reverse_grid:
#         # PRINT NORTH CONNECTION ROW
#         str += "#"
#         for room in row:
#             if room is not None and room.n_to is not None:
#                 str += "  |  "
#             else:
#                 str += "     "
#         str += "#\n"
#         # PRINT ROOM ROW
#         str += "#"
#         for room in row:
#             if room is not None and room.w_to is not None:
#                 str += "-"
#             else:
#                 str += " "
#             if room is not None:
#                 str += f"{room.id}".zfill(3)
#             else:
#                 str += "   "
#             if room is not None and room.e_to is not None:
#                 str += "-"
#             else:
#                 str += " "
#         str += "#\n"
#         # PRINT SOUTH CONNECTION ROW
#         str += "#"
#         for room in row:
#             if room is not None and room.s_to is not None:
#                 str += "  |  "
#             else:
#                 str += "     "
#         str += "#\n"
#
#     # Add bottom border
#     str += "# " * ((3 + self.width * 5) // 2) + "\n"
#
#     # Print string
#     print(str)