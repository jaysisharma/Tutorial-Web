const express = require('express')
const mongoose = require('mongoose')
const app = express()
const PORT = 8000

const db = () =>{
try {
    mongoose.connect("mongodb+srv://jaysisharma9817:xC0lXMw21DOxN4i1@cluster0.svtg6up.mongodb.net/")
    console.log("Database Connected Successfully")
} catch (error) {
    console.log("An error occured", error)
}
}
db()

// sqp_5677f429105b8ff58f65384086a676731fe5fea7

// jaysisharma9817

// xC0lXMw21DOxN4i1

app.listen(PORT,()=>{
    console.log("Server is running on Port 8000")
})