extern crate reqwest;

use std::collections::HashMap;




fn main() -> Result<(), Box<std::error::Error>> {

    // Simple GET
    let mut get_response = reqwest::get("http://localhost:8000")?;
    println!("{:#?}", get_response);
    println!("{:#?}", get_response.text()?);
    // To get JSON response
    // get_response.json()?

    // Posting JSON
    // Check out serde_json crate
    let mut map = HashMap::new();
    map.insert("key1", "value1");
    map.insert("key2", "value2");

    let client = reqwest::Client::new();
    let mut post_response = client.post("http://httpbin.org/post")
        .json(&map)
        .send()?;
    println!("{:?}", post_response.text()?);

    return Ok(())
}