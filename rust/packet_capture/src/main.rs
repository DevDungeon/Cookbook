extern crate pcap;

fn main() {

    // list all of the devices pcap tells us are available
    for device in pcap::Device::list().unwrap() {
        println!("Found device: {:?}", device);

        // now you can create a Capture with this Device if you want.
        let mut capture_device = device.open().unwrap();

        // get a packet from this capture
        let packet = capture_device.next();

        println!("got a packet! {:?}", packet);
    }
}