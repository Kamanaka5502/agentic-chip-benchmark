import time

class MetricsCollector:
    def __init__(self):
        self.latencies = []
        self.total_tokens = 0
        self.start_time = time.time()

    def record(self, latency):
        self.latencies.append(latency)

    def percentile(self, percent):
        data = sorted(self.latencies)
        if not data:
            return 0
        k = (len(data)-1) * (percent/100)
        f = int(k)
        c = min(f+1, len(data)-1)
        if f == c:
            return data[int(k)]
        return data[f] + (data[c] - data[f]) * (k - f)

    def report(self):
        if not self.latencies:
            print("No data.")
            return

        elapsed = time.time() - self.start_time

        print("\n--- Benchmark Report ---")
        print("Total Requests:", len(self.latencies))
        print("P50 Latency:", round(self.percentile(50), 4))
        print("P95 Latency:", round(self.percentile(95), 4))
        print("P99 Latency:", round(self.percentile(99), 4))
        print("Mean Latency:", round(sum(self.latencies)/len(self.latencies), 4))
        print("Total Tokens:", self.total_tokens)
        print("Tokens/sec:", round(self.total_tokens / elapsed, 2))
        print("Elapsed Time:", round(elapsed, 2), "seconds")
