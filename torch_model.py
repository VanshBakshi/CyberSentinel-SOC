from pathlib import Path

def train_autoencoder(events, epochs=8):
    try:
        import torch
        from torch import nn
    except ImportError as exc:
        raise RuntimeError("PyTorch is not installed") from exc
    if len(events) < 20:
        raise ValueError("At least 20 events are required")
    import numpy as np
    X = np.array([[e.bytes_in or 0, e.bytes_out or 0, e.failed_logins or 0, e.threat_score or 0, len(e.message or ""), e.risk_score or 0] for e in events], dtype=np.float32)
    scale = np.maximum(X.std(axis=0), 1e-6); mean = X.mean(axis=0); X = (X-mean)/scale
    data = torch.tensor(X)
    model = nn.Sequential(nn.Linear(6, 12), nn.ReLU(), nn.Linear(12, 3), nn.ReLU(), nn.Linear(3, 12), nn.ReLU(), nn.Linear(12, 6))
    opt = torch.optim.Adam(model.parameters(), lr=0.001); loss_fn = nn.MSELoss()
    model.train()
    for _ in range(epochs):
        opt.zero_grad(); loss = loss_fn(model(data), data); loss.backward(); opt.step()
    path = Path("models/torch_autoencoder.pt"); path.parent.mkdir(exist_ok=True); torch.save({"state_dict": model.state_dict(), "mean": mean.tolist(), "std": scale.tolist()}, path)
    return {"epochs": epochs, "loss": float(loss.item()), "samples": len(events)}
