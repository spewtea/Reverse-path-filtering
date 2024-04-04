def unicast_reverse_path_forwarding(source_ip, destination_ip, routing_table):

    """Performs unicast reverse path forwarding.
    Args:
        source_ip: The IP address of the source.
        destination_ip: The IP address of the destination.
        routing_table: A dictionary mapping destination IP addresses to next-hop IP addresses.
    Returns:
        The next-hop IP address for the destination, or None if no path is found.
    """

    # Create a reverse routing table.
    reverse_routing_table = {}
    for destination_ip, next_hop_ip in routing_table.items():
        if next_hop_ip not in reverse_routing_table:
            reverse_routing_table[next_hop_ip] = []
        reverse_routing_table[next_hop_ip].append(destination_ip)

    # Start at the destination and work our way back to the source.
    current_ip = destination_ip
    visited_ips = set()
    while current_ip != source_ip:
        
        if current_ip in visited_ips:
            # Loop detected, break the loop
            return None
        visited_ips.add(current_ip)
        next_hop_ips = reverse_routing_table.get(current_ip)
        if next_hop_ips is None:
            return None
        # Choose the first next-hop IP in the list
        next_hop_ip = next_hop_ips[0]
        current_ip = next_hop_ip
        
    s1=dict(reversed(list(reverse_routing_table.items())))
    print(s1)
    
    # We have found a path back to the source.
    return next_hop_ip

# Example usage:

routing_table = {
    "192.168.0.101": "192.168.1.100",
    "192.168.1.100": "10.0.0.1",
    "10.0.0.1": "192.168.1.1"
}
source_ip = str("192.168.0.101")
print(source_ip)
destination_ip = str("10.0.0.1")
print(destination_ip)

next_hop_ip = unicast_reverse_path_forwarding(source_ip, destination_ip, routing_table)

if next_hop_ip is None:
    print("No path found.")
else:
    print("The next-hop source IP address is:", next_hop_ip)