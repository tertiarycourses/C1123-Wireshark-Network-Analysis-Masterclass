# Synthetic fixture provenance

Created entirely offline for C1123. No traffic is sent by the generator. Branch-office packets are authored with Scapy; TLS uses a real Python ssl MemoryBIO handshake with a temporary self-signed certificate, wrapped in synthetic TCP. The private certificate key is discarded. lab-tls.keys contains deliberately shareable secrets for this fictional session only. TLS capture and key log must be regenerated together. Packet timings are constructed for learning; they are not production measurements.
