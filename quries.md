db.user.aggregate([
   {
      $lookup:
         {
            from: "carousell",
            localField: "_id",
            foreignField: "userid",
            as: "userlisting"
        }
   }
])