# Graph notes — Lab 15

| Graph | Stream / filter | Interval | Unit | Visible pattern | Limitation |
|---|---|---|---|---|---|
| Time/Sequence (Stevens) | tcp.stream == 3 | — | sequence number | | |
| I/O — retransmissions | tcp.analysis.retransmission | 1 s | packets | | |
| I/O — zero window | tcp.analysis.zero_window | 1 s | packets | | |
| Round Trip Time | tcp.stream == 3 | — | seconds | | |
