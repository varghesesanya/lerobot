import argparse
import time

from lerobot.common.datasets.lerobot_dataset import LeRobotDataset
from lerobot.scripts.visualize_dataset import visualize_dataset

def main():
    parser = argparse.ArgumentParser(description="Visualize LeRobot dataset locally.")
    parser.add_argument("--root", required=True, help="Path to local dataset folder")
    parser.add_argument("--episode-index", type=int, required=True, help="Index of the episode to visualize")
    parser.add_argument("--mode", type=str, choices=["rgb", "depth"], default="rgb")
    parser.add_argument("--web-port", type=int, default=8080)
    parser.add_argument("--ws-port", type=int, default=8765)
    args = parser.parse_args()

    # Load dataset from local folder
    dataset = LeRobotDataset.from_local(root=args.root)

    print(f"Loaded dataset from {args.root} with {len(dataset)} episodes.")
    episode = dataset[args.episode_index]

    # Start the visualization
    # start_visualizer(
    #     episode=episode,
    #     mode=args.mode,
    #     web_port=args.web_port,
    #     ws_port=args.ws_port,
    # )
    
    visualize_dataset(
        dataset,
        episode_index=0,
        batch_size=32,
        save=True
    )

    # Keep server running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")

if __name__ == "__main__":
    main()
